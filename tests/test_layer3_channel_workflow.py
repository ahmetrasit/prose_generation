from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "_channel" / "layer3" / "scripts"
sys.path.insert(0, str(SCRIPTS))

import build_packet as layer3_build  # noqa: E402
import instantiate as layer3_instantiate  # noqa: E402
import validate as layer3_validate  # noqa: E402


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def test_packet_runs_without_optional_source_families(tmp_path: Path) -> None:
    quran_data = tmp_path / "quran-data"
    latent = tmp_path / "latent_activation"
    layer2 = tmp_path / "layer2"
    write(
        quran_data / "data" / "text" / "quran-uthmani.tsv",
        "42:0|basmala\n42:1|ayah surface\n",
    )
    write(layer2 / "42_1.prose.test.md", "Ordinary reader prose.\n")
    write(layer2 / "42_1.evidence.test.md", "Local evidence.\n")

    packet = layer3_build.build_packet(
        surah=42,
        language="tr",
        layer2_dir=layer2,
        layer2_label="test",
        quran_data=quran_data,
        latent_activation=latent,
    )

    assert packet["coverage"]["networkV3"]["status"] == "absent"
    assert packet["coverage"]["v11"]["status"] == "absent"
    assert any(
        "network-v3" in warning and "absent" in warning
        for warning in packet["warnings"]
    )
    assert any("V11 is absent" in warning for warning in packet["warnings"])
    assert layer3_validate.validate_packet(packet) == []


def test_packet_uses_reviewed_network_synthesis_only(tmp_path: Path) -> None:
    quran_data = tmp_path / "quran-data"
    latent = tmp_path / "latent_activation"
    layer2 = tmp_path / "layer2"
    network = (
        quran_data
        / "data"
        / "analysis"
        / "channels"
        / "network-v3"
        / "s042"
    )
    write(
        quran_data / "data" / "text" / "quran-uthmani.tsv",
        "42:0|basmala\n42:1|ayah surface\n",
    )
    write(layer2 / "42_1.prose.test.md", "Ordinary reader prose.\n")
    write(layer2 / "42_1.evidence.test.md", "Local evidence.\n")
    write(network / "review" / "reader_a_pilot.md", "CURATED_NETWORK_REVIEW\n")
    write(network / "channel_candidates.jsonl", '{"raw":"candidate"}\n')
    write(
        network / "families" / "channel_families.jsonl",
        '{"raw":"family"}\n',
    )

    packet = layer3_build.build_packet(
        surah=42,
        language="tr",
        layer2_dir=layer2,
        layer2_label="test",
        quran_data=quran_data,
        latent_activation=latent,
    )

    network_sources = [
        source
        for source in packet["sourceRegistry"]
        if source["sourceId"].startswith("network-")
    ]
    assert [source["sourceId"] for source in network_sources] == ["network-review"]
    assert packet["evidenceField"]["reviewedChannels"] == [
        {
            "synthesisId": "network-v3-reviewed",
            "sourceRefs": ["network-review"],
            "text": "CURATED_NETWORK_REVIEW\n",
        }
    ]
    assert packet["coverage"]["networkV3"]["status"] == "complete"


def test_layer2_boundary_projection_uses_explicit_headings() -> None:
    markdown = """\
**A result is produced and retained**

Routine support.

## Preserved rejected readings

- Rejected claim and its surviving contribution.

## Coverage note

Production detail.
"""

    assert layer3_build.extract_layer2_boundaries(markdown) == [
        "## Preserved rejected readings\n\n"
        "- Rejected claim and its surviving contribution."
    ]


def test_discovery_prompt_is_hermetic(tmp_path: Path) -> None:
    packet = {
        "schemaVersion": "layer3-source-packet-v2",
        "packetId": "s042-tr-layer3-v2",
        "surah": 42,
        "language": "tr",
        "sourceRegistry": [
            {
                "sourceId": "quran-text",
                "kind": "quran-text",
                "role": "primary-ground",
                "path": "quran-data/data/text/quran-uthmani.tsv",
                "format": "tsv",
                "projection": "Surah rows.",
            }
        ],
        "primaryGround": {
            "sourceRefs": ["quran-text"],
            "ayahs": [
                {
                    "ayahRef": "42:1",
                    "unitType": "ayah",
                    "arabic": "surface",
                    "reading": {
                        "sourceRef": "quran-text",
                        "text": "ONLY_INLINED_CONTENT",
                    },
                }
            ],
        },
        "evidenceField": {
            "localBoundaries": [],
            "reviewedChannels": [
                {
                    "synthesisId": "network-v3-reviewed",
                    "sourceRefs": ["network-review"],
                    "text": """\
# Review

### 1. LEAKED_PARENT_TITLE
- Surface relation: indirect; reviewed surface note.

#### Subchannel A. LEAKED_SUBCHANNEL_TITLE
- Reading type: latent/lexical
- Scene or process: PREWRITTEN_SCENE
- Active motifs: REVIEWED_SIGNAL (`x:B001/m01`)
- Ayah anchors: 42:1 `surface`
- Synthesis: PREWRITTEN_SYNTHESIS
""",
                }
            ],
            "legacyIntegration": [],
        },
        "coverage": {
            name: {
                "status": "complete" if name == "quranText" else "absent",
                "required": name in {"quranText", "layer2"},
                "sourceIds": ["quran-text"] if name == "quranText" else [],
                "missing": [],
                "notes": [],
            }
            for name in ("quranText", "layer2", "networkV3", "v11")
        },
        "warnings": [],
    }
    packet_path = tmp_path / "packet.json"
    layer3_build.write_json(packet_path, packet)

    prompt = layer3_instantiate.assemble(
        stage="discover",
        surah=42,
        packet_path=packet_path,
        candidates_path=None,
        ledger_path=None,
    )

    assert "ONLY_INLINED_CONTENT" not in prompt
    assert "PREWRITTEN_SCENE" not in prompt
    assert "PREWRITTEN_SYNTHESIS" not in prompt
    assert "LEAKED_PARENT_TITLE" not in prompt
    assert "LEAKED_SUBCHANNEL_TITLE" not in prompt
    assert "REVIEWED_SIGNAL" in prompt
    assert "network-p01-a" in prompt
    assert '"readingType"' not in prompt
    assert '"surfaceRelation"' not in prompt
    assert '"reviewStatus"' not in prompt
    assert "<BEGIN_DISCOVERY_INPUT_JSON>" in prompt
    assert "<END_DISCOVERY_INPUT_JSON>" in prompt
    assert "<BEGIN_SOURCE_PACKET_JSON>" not in prompt
    assert "Paths inside the packet are provenance labels" in prompt
    assert "Do not call tools or edit files" in prompt


def test_discovery_prompt_has_no_candidate_or_length_target() -> None:
    prompt = (ROOT / "_channel" / "layer3" / "prompts" / "01-discover.md").read_text(
        encoding="utf-8"
    )

    folded = prompt.casefold()
    for forbidden in (
        "prefer fewer",
        "two to four",
        "at most",
        "up to",
        "maximum number",
        "minimum number",
        "length target",
    ):
        assert forbidden not in folded

    schema = (
        ROOT
        / "_channel"
        / "layer3"
        / "schemas"
        / "discovery-hypotheses-v1.schema.json"
    ).read_text(encoding="utf-8")
    assert "latentSignalDependence" not in schema
    assert '"risk"' not in schema
