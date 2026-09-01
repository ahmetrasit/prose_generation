#!/usr/bin/env python3
"""Standalone CLI for the commentary v3 workflow."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import render_authoring

from v3lib.adjudication import (
    ADJUDICATION_RESPONSE_SAFETY_CEILING,
    AdjudicationOptions,
    render_adjudication_for_ayah,
    validate_adjudication_for_ayah,
)
from v3lib.common import (
    OUTPUTS_ROOT,
    ScopeError,
    ValidationError,
    WorkflowError,
    confined_existing_file,
    load_json_object_bounded,
)
from v3lib.prepare import PrepareOptions, prepare_bundle_file
from v3lib.synthesis import (
    SynthesisOptions,
    render_synthesis_for_ayah,
    validate_synthesis_for_ayah,
    verify_final_outputs_for_ayah,
)


def _add_handoff_prepare_options(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "--hft-policy", choices=("strict", "quarantine"), default="strict"
    )
    parser.add_argument("--allow-legacy-hft-response", action="store_true")
    parser.add_argument("--allow-incomplete-branch-coverage", action="store_true")
    parser.add_argument("--max-optional-candidates", type=int, default=40)
    parser.add_argument("--max-support-chars", type=int, default=1_600)
    parser.add_argument("--max-support-per-candidate", type=int, default=5)
    parser.add_argument("--max-branch-bytes-per-root", type=int, default=32_000)
    parser.add_argument("--max-pericope-ayahs", type=int, default=512)
    parser.add_argument("--max-docket-bytes", type=int, default=500_000)


def _add_synthesis_options(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--max-packet-bytes", type=int, default=4_000_000)
    parser.add_argument("--max-prompt-bytes", type=int, default=5_000_000)
    parser.add_argument("--max-response-bytes", type=int, default=32_000_000)
    parser.add_argument("--max-annotation-chars", type=int, default=1_000_000)
    parser.add_argument("--min-prose-chars", type=int, default=500)
    parser.add_argument("--max-prose-chars", type=int, default=1_000_000)
    parser.add_argument(
        "--max-rendered-output-bytes", type=int, default=64_000_000
    )


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Prepare, adjudicate, and synthesize commentary v3 artifacts."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)
    advance = subparsers.add_parser(
        "advance",
        help=(
            "Run the complete deterministic workflow until a model response is needed "
            "or final verification succeeds."
        ),
    )
    advance.add_argument("--bundle", required=True, type=Path)
    advance.add_argument(
        "--hft-policy",
        choices=("strict", "quarantine"),
        default="strict",
    )
    advance.add_argument("--allow-legacy-hft-response", action="store_true")
    advance.add_argument(
        "--allow-incomplete-branch-coverage",
        action="store_true",
        help=(
            "Explicitly authorize model handoff when a focus-root dictionary is "
            "null and the degraded coverage is recorded."
        ),
    )
    advance.add_argument(
        "--force",
        action="store_true",
        help="Deliberately replace changed generated artifacts at every reached stage.",
    )
    advance.add_argument("--max-optional-candidates", type=int, default=40)
    advance.add_argument("--max-support-chars", type=int, default=1_600)
    advance.add_argument("--max-support-per-candidate", type=int, default=5)
    advance.add_argument("--max-branch-bytes-per-root", type=int, default=32_000)
    advance.add_argument("--max-pericope-ayahs", type=int, default=512)
    advance.add_argument("--max-docket-bytes", type=int, default=500_000)
    advance.add_argument(
        "--max-adjudication-prompt-bytes", type=int, default=750_000
    )
    _add_synthesis_options(advance)

    authoring_advance = subparsers.add_parser(
        "authoring-advance",
        help=(
            "Advance the complete prose-first workflow to its next path-only "
            "agent handoff or verified completion."
        ),
    )
    authoring_advance.add_argument("--ayah", required=True)
    authoring_advance.add_argument("--docket", type=Path)
    authoring_advance.add_argument("--source-bundle", type=Path)
    authoring_advance.add_argument(
        "--inter-ayah-dir",
        type=Path,
        default=render_authoring.DEFAULT_INTER_AYAH_DIR,
    )
    authoring_advance.add_argument(
        "--inter-ayah-parent-dir",
        type=Path,
        default=render_authoring.DEFAULT_INTER_AYAH_PARENT_DIR,
    )
    authoring_advance.add_argument(
        "--quran-text",
        type=Path,
        default=render_authoring.DEFAULT_QURAN_TEXT,
    )

    authoring_record_session = subparsers.add_parser(
        "authoring-record-session",
        help="Bind a persisted agent session to a canonical authoring conversation.",
    )
    authoring_record_session.add_argument("--ayah", required=True)
    authoring_record_session.add_argument(
        "--conversation",
        required=True,
        choices=(
            "scope-micro",
            "scope-macro",
            "scope-global",
            "scope-reconciler",
            "canonical-writer",
        ),
    )
    authoring_record_session.add_argument("--session-id", required=True)
    authoring_record_session.add_argument(
        "--prompt-manifest", required=True, type=Path
    )

    authoring_record_turn = subparsers.add_parser(
        "authoring-record-turn",
        help="Bind a completed canonical writer turn to its exact output hashes.",
    )
    authoring_record_turn.add_argument("--ayah", required=True)
    authoring_record_turn.add_argument("--session-id", required=True)
    authoring_record_turn.add_argument(
        "--prompt-manifest", required=True, type=Path
    )
    authoring_record_turn.add_argument("--prior-receipt", type=Path)

    prepare = subparsers.add_parser(
        "prepare", help="Audit one source bundle and build an adjudication docket."
    )
    prepare.add_argument("--bundle", required=True, type=Path)
    prepare.add_argument(
        "--hft-policy",
        choices=("strict", "quarantine"),
        default="strict",
        help="Strict fails on malformed HFT; quarantine keeps it out of the docket.",
    )
    prepare.add_argument(
        "--allow-legacy-hft-response",
        action="store_true",
        help=(
            "Admit a scope-valid HFT response that lacks a packet identity echo; "
            "disabled by default."
        ),
    )
    prepare.add_argument(
        "--allow-incomplete-branch-coverage",
        action="store_true",
        help=(
            "Prepare a model-ready degraded docket despite explicitly null "
            "focus-root dictionaries."
        ),
    )
    prepare.add_argument("--max-optional-candidates", type=int, default=40)
    prepare.add_argument("--max-support-chars", type=int, default=1_600)
    prepare.add_argument("--max-support-per-candidate", type=int, default=5)
    prepare.add_argument("--max-branch-bytes-per-root", type=int, default=32_000)
    prepare.add_argument("--max-pericope-ayahs", type=int, default=512)
    prepare.add_argument("--max-docket-bytes", type=int, default=500_000)
    prepare.add_argument(
        "--dry-run",
        action="store_true",
        help="Validate and report without writing artifacts.",
    )
    prepare.add_argument(
        "--force",
        action="store_true",
        help="Replace an existing artifact only when replacement is deliberate.",
    )

    render_adjudication = subparsers.add_parser(
        "render-adjudication",
        help="Render the bounded model prompt from a ready adjudication docket.",
    )
    render_adjudication.add_argument("--ayah", required=True)
    _add_handoff_prepare_options(render_adjudication)
    render_adjudication.add_argument("--max-prompt-bytes", type=int, default=750_000)
    render_adjudication.add_argument("--dry-run", action="store_true")
    render_adjudication.add_argument("--force", action="store_true")

    validate_adjudication = subparsers.add_parser(
        "validate-adjudication",
        help="Validate the fixed raw model response and publish a normalized artifact.",
    )
    validate_adjudication.add_argument("--ayah", required=True)
    _add_handoff_prepare_options(validate_adjudication)
    validate_adjudication.add_argument("--dry-run", action="store_true")
    validate_adjudication.add_argument("--force", action="store_true")

    render_synthesis = subparsers.add_parser(
        "render-synthesis",
        help="Build the selected-evidence packet and constrained synthesis prompt.",
    )
    render_synthesis.add_argument("--ayah", required=True)
    _add_handoff_prepare_options(render_synthesis)
    _add_synthesis_options(render_synthesis)
    render_synthesis.add_argument("--dry-run", action="store_true")
    render_synthesis.add_argument("--force", action="store_true")

    validate_synthesis = subparsers.add_parser(
        "validate-synthesis",
        help="Validate the raw synthesis response and publish all four final files.",
    )
    validate_synthesis.add_argument("--ayah", required=True)
    _add_handoff_prepare_options(validate_synthesis)
    _add_synthesis_options(validate_synthesis)
    validate_synthesis.add_argument("--dry-run", action="store_true")
    validate_synthesis.add_argument("--force", action="store_true")

    verify = subparsers.add_parser(
        "verify", help="Revalidate the complete lineage and byte-check all final outputs."
    )
    verify.add_argument("--ayah", required=True)
    _add_handoff_prepare_options(verify)
    _add_synthesis_options(verify)
    return parser


def _prepare_options(args: argparse.Namespace) -> PrepareOptions:
    return PrepareOptions(
        hft_policy=args.hft_policy,
        allow_legacy_hft_response=args.allow_legacy_hft_response,
        allow_incomplete_branch_coverage=args.allow_incomplete_branch_coverage,
        max_optional_candidates=args.max_optional_candidates,
        max_support_chars=args.max_support_chars,
        max_support_per_candidate=args.max_support_per_candidate,
        max_branch_bytes_per_root=args.max_branch_bytes_per_root,
        max_pericope_ayahs=args.max_pericope_ayahs,
        max_docket_bytes=args.max_docket_bytes,
    )


def _adjudication_options(args: argparse.Namespace) -> AdjudicationOptions:
    defaults = AdjudicationOptions()
    if hasattr(args, "max_adjudication_prompt_bytes"):
        max_prompt_bytes = args.max_adjudication_prompt_bytes
    elif getattr(args, "command", None) == "render-adjudication":
        max_prompt_bytes = args.max_prompt_bytes
    else:
        max_prompt_bytes = defaults.max_prompt_bytes
    return AdjudicationOptions(max_prompt_bytes=max_prompt_bytes)


def _run_prepare(args: argparse.Namespace) -> int:
    options = _prepare_options(args)
    prepared, docket, paths = prepare_bundle_file(
        args.bundle,
        options=options,
        write=not args.dry_run,
        force=args.force,
    )
    result = {
        "status": "ok",
        "command": "prepare",
        "dry_run": args.dry_run,
        "ayah_ref": prepared["identity"]["ayah_ref"],
        "readiness_mode": prepared["readiness"]["mode"],
        "readiness_warnings": prepared["readiness"]["warnings"],
        "readiness_blockers": prepared["readiness"]["blockers"],
        "readiness_degraded_reasons": prepared["readiness"]["degraded_reasons"],
        "mandatory_candidates_ready": prepared["mandatory_candidates_ready"],
        "hft_status": prepared["scope_audit"]["hft"]["status"],
        "focus_root_branch_coverage": docket["scope"]["branch_coverage"],
        "candidate_count": len(docket["candidates"]),
        "docket_bytes": prepared["budget"]["docket_bytes"],
        "paths": paths if not args.dry_run else None,
    }
    print(json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2))
    return 0


def _run_authoring_advance(args: argparse.Namespace) -> int:
    result = render_authoring.advance_authoring(args)
    print(json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2))
    return 0


def _run_authoring_record_session(args: argparse.Namespace) -> int:
    result = render_authoring.record_authoring_session(args)
    print(json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2))
    return 0


def _run_authoring_record_turn(args: argparse.Namespace) -> int:
    result = render_authoring.record_authoring_turn(args)
    print(json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2))
    return 0


def _raw_response_is_present(path_value: str) -> bool:
    return _raw_response_state(path_value, expected_identity={}) != "missing"


def _raw_response_state(
    path_value: str,
    *,
    expected_identity: dict[str, str],
    max_bytes: int = ADJUDICATION_RESPONSE_SAFETY_CEILING,
) -> str:
    path = Path(path_value)
    try:
        relative = path.absolute().relative_to(OUTPUTS_ROOT.absolute())
    except ValueError as exc:
        raise ValidationError(
            f"Expected response path is outside v3 outputs: {path}"
        ) from exc
    if not path.exists() and not path.is_symlink():
        return "missing"
    response_path = confined_existing_file(OUTPUTS_ROOT, relative)
    try:
        response, _raw = load_json_object_bounded(
            response_path, max_bytes=max_bytes
        )
    except ValidationError:
        return "invalid"
    identity = response.get("identity")
    if expected_identity:
        if not isinstance(identity, dict) or set(identity) != set(expected_identity):
            return "invalid"
        if any(
            identity[field] != value
            for field, value in expected_identity.items()
        ):
            return "stale"
    return "current"


def _response_next_action(response_state: str) -> str:
    if response_state == "stale":
        return (
            "Replace the stale response with the contracted JSON at "
            "expected_response, then rerun this command."
        )
    if response_state == "invalid":
        return (
            "Replace the malformed or contract-incomplete response with the "
            "contracted JSON at expected_response, then rerun this command."
        )
    return (
        "Submit the prompt and adjacent manifest identity to a model, write only "
        "the contracted JSON response at expected_response, then rerun this command."
    )


def _run_advance(args: argparse.Namespace) -> int:
    prepare_options = _prepare_options(args)
    adjudication_options = _adjudication_options(args)
    synthesis_options = _synthesis_options(args)
    prepared, docket, prepare_paths = prepare_bundle_file(
        args.bundle,
        options=prepare_options,
        force=args.force,
    )
    ayah_ref = prepared["identity"]["ayah_ref"]
    _adjudication_prompt, adjudication_manifest, adjudication_paths = (
        render_adjudication_for_ayah(
            ayah_ref,
            options=adjudication_options,
            prepare_options=prepare_options,
            force=args.force,
        )
    )
    common = {
        "command": "advance",
        "ayah_ref": ayah_ref,
        "readiness_mode": prepared["readiness"]["mode"],
        "readiness_warnings": prepared["readiness"]["warnings"],
        "readiness_degraded_reasons": prepared["readiness"]["degraded_reasons"],
        "candidate_count": len(docket["candidates"]),
        "focus_root_branch_coverage": docket["scope"]["branch_coverage"],
        "source_bundle": prepare_paths["source_bundle"],
    }
    adjudication_response_state = _raw_response_state(
        adjudication_paths["expected_response"],
        expected_identity=adjudication_manifest["identity"],
    )
    if adjudication_response_state != "current":
        print(
            json.dumps(
                {
                    "status": "waiting_for_model",
                    "stage": "adjudication",
                    **common,
                    "prompt": adjudication_paths["prompt"],
                    "prompt_manifest": adjudication_paths["prompt_manifest"],
                    "expected_response": adjudication_paths["expected_response"],
                    "response_state": adjudication_response_state,
                    "prompt_bytes": adjudication_manifest["budget"]["prompt_bytes"],
                    "next_action": _response_next_action(
                        adjudication_response_state
                    ),
                },
                ensure_ascii=False,
                sort_keys=True,
                indent=2,
            )
        )
        return 0

    adjudication, adjudication_validated_paths = validate_adjudication_for_ayah(
        ayah_ref,
        options=adjudication_options,
        prepare_options=prepare_options,
        force=args.force,
    )
    packet, _synthesis_prompt, synthesis_manifest, synthesis_paths = (
        render_synthesis_for_ayah(
            ayah_ref,
            options=synthesis_options,
            adjudication_options=adjudication_options,
            prepare_options=prepare_options,
            force=args.force,
        )
    )
    synthesis_response_state = _raw_response_state(
        synthesis_paths["expected_response"],
        expected_identity=synthesis_manifest["identity"],
        max_bytes=synthesis_options.max_response_bytes,
    )
    if synthesis_response_state != "current":
        print(
            json.dumps(
                {
                    "status": "waiting_for_model",
                    "stage": "synthesis",
                    **common,
                    "adjudication_coverage": adjudication["coverage"],
                    "validated_adjudication": adjudication_validated_paths["validated"],
                    "selected_candidate_count": len(packet["selections"]),
                    "prompt": synthesis_paths["prompt"],
                    "prompt_manifest": synthesis_paths["prompt_manifest"],
                    "expected_response": synthesis_paths["expected_response"],
                    "response_state": synthesis_response_state,
                    "prompt_bytes": synthesis_manifest["budget"]["prompt_bytes"],
                    "next_action": _response_next_action(
                        synthesis_response_state
                    ),
                },
                ensure_ascii=False,
                sort_keys=True,
                indent=2,
            )
        )
        return 0

    synthesis, _outputs, synthesis_validated_paths = validate_synthesis_for_ayah(
        ayah_ref,
        options=synthesis_options,
        adjudication_options=adjudication_options,
        prepare_options=prepare_options,
        force=args.force,
    )
    verification = verify_final_outputs_for_ayah(
        ayah_ref,
        options=synthesis_options,
        adjudication_options=adjudication_options,
        prepare_options=prepare_options,
    )
    print(
        json.dumps(
            {
                "status": "ok",
                "stage": "complete",
                **common,
                "adjudication_coverage": adjudication["coverage"],
                "synthesis_coverage": synthesis["coverage"],
                "validated_synthesis": synthesis_validated_paths["validated"],
                "verification": verification,
            },
            ensure_ascii=False,
            sort_keys=True,
            indent=2,
        )
    )
    return 0


def _run_render_adjudication(args: argparse.Namespace) -> int:
    options = _adjudication_options(args)
    _prompt, manifest, paths = render_adjudication_for_ayah(
        args.ayah,
        options=options,
        prepare_options=_prepare_options(args),
        write=not args.dry_run,
        force=args.force,
    )
    print(
        json.dumps(
            {
                "status": "ok",
                "command": "render-adjudication",
                "dry_run": args.dry_run,
                "ayah_ref": args.ayah,
                "candidate_count": manifest["budget"]["candidate_count"],
                "prompt_bytes": manifest["budget"]["prompt_bytes"],
                "estimated_tokens_chars_div_4": manifest["budget"][
                    "estimated_tokens_chars_div_4"
                ],
                "paths": paths if not args.dry_run else None,
            },
            ensure_ascii=False,
            sort_keys=True,
            indent=2,
        )
    )
    return 0


def _run_validate_adjudication(args: argparse.Namespace) -> int:
    artifact, paths = validate_adjudication_for_ayah(
        args.ayah,
        options=_adjudication_options(args),
        prepare_options=_prepare_options(args),
        write=not args.dry_run,
        force=args.force,
    )
    print(
        json.dumps(
            {
                "status": "ok",
                "command": "validate-adjudication",
                "dry_run": args.dry_run,
                "ayah_ref": args.ayah,
                "coverage": artifact["coverage"],
                "paths": paths if not args.dry_run else None,
            },
            ensure_ascii=False,
            sort_keys=True,
            indent=2,
        )
    )
    return 0


def _synthesis_options(args: argparse.Namespace) -> SynthesisOptions:
    defaults = SynthesisOptions()
    return SynthesisOptions(
        **{
            field: getattr(args, field, getattr(defaults, field))
            for field in (
                "max_packet_bytes",
                "max_prompt_bytes",
                "max_response_bytes",
                "max_annotation_chars",
                "min_prose_chars",
                "max_prose_chars",
                "max_rendered_output_bytes",
            )
        }
    )


def _run_render_synthesis(args: argparse.Namespace) -> int:
    packet, _prompt, manifest, paths = render_synthesis_for_ayah(
        args.ayah,
        options=_synthesis_options(args),
        adjudication_options=_adjudication_options(args),
        prepare_options=_prepare_options(args),
        write=not args.dry_run,
        force=args.force,
    )
    print(
        json.dumps(
            {
                "status": "ok",
                "command": "render-synthesis",
                "dry_run": args.dry_run,
                "ayah_ref": args.ayah,
                "selected_candidate_count": len(packet["selections"]),
                "packet_bytes": manifest["budget"]["packet_bytes"],
                "prompt_bytes": manifest["budget"]["prompt_bytes"],
                "estimated_tokens_chars_div_4": manifest["budget"][
                    "estimated_tokens_chars_div_4"
                ],
                "paths": paths if not args.dry_run else None,
            },
            ensure_ascii=False,
            sort_keys=True,
            indent=2,
        )
    )
    return 0


def _run_validate_synthesis(args: argparse.Namespace) -> int:
    artifact, _outputs, paths = validate_synthesis_for_ayah(
        args.ayah,
        options=_synthesis_options(args),
        adjudication_options=_adjudication_options(args),
        prepare_options=_prepare_options(args),
        write=not args.dry_run,
        force=args.force,
    )
    print(
        json.dumps(
            {
                "status": "ok",
                "command": "validate-synthesis",
                "dry_run": args.dry_run,
                "ayah_ref": args.ayah,
                "coverage": artifact["coverage"],
                "paths": paths if not args.dry_run else None,
            },
            ensure_ascii=False,
            sort_keys=True,
            indent=2,
        )
    )
    return 0


def _run_verify(args: argparse.Namespace) -> int:
    result = verify_final_outputs_for_ayah(
        args.ayah,
        options=_synthesis_options(args),
        adjudication_options=_adjudication_options(args),
        prepare_options=_prepare_options(args),
    )
    print(
        json.dumps(
            {"status": "ok", "command": "verify", **result},
            ensure_ascii=False,
            sort_keys=True,
            indent=2,
        )
    )
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)
    try:
        if args.command == "advance":
            return _run_advance(args)
        if args.command == "authoring-advance":
            return _run_authoring_advance(args)
        if args.command == "authoring-record-session":
            return _run_authoring_record_session(args)
        if args.command == "authoring-record-turn":
            return _run_authoring_record_turn(args)
        if args.command == "prepare":
            return _run_prepare(args)
        if args.command == "render-adjudication":
            return _run_render_adjudication(args)
        if args.command == "validate-adjudication":
            return _run_validate_adjudication(args)
        if args.command == "render-synthesis":
            return _run_render_synthesis(args)
        if args.command == "validate-synthesis":
            return _run_validate_synthesis(args)
        if args.command == "verify":
            return _run_verify(args)
        parser.error(f"Unknown command: {args.command}")
    except ScopeError as exc:
        print(
            json.dumps(
                {
                    "status": "error",
                    "error_type": "scope_error",
                    "message": str(exc),
                    "report": exc.report,
                },
                ensure_ascii=False,
                sort_keys=True,
                indent=2,
            ),
            file=sys.stderr,
        )
        return 2
    except WorkflowError as exc:
        print(
            json.dumps(
                {
                    "status": "error",
                    "error_type": type(exc).__name__,
                    "message": str(exc),
                },
                ensure_ascii=False,
                sort_keys=True,
                indent=2,
            ),
            file=sys.stderr,
        )
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
