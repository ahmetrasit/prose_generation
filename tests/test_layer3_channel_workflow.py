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
    assert packet["coverage"]["v12"]["status"] == "absent"
    assert any("network-v3 is absent" in warning for warning in packet["warnings"])
    assert any("V11 is absent" in warning for warning in packet["warnings"])
    assert layer3_validate.validate_packet(packet) == []


def test_discovery_prompt_is_hermetic(tmp_path: Path) -> None:
    packet = {
        "schemaVersion": "layer3-source-packet-v1",
        "packetId": "s042-tr-layer3-v1",
        "surah": 42,
        "language": "tr",
        "ayahs": [
            {
                "ayahRef": "42:1",
                "unitType": "ayah",
                "arabic": "surface",
                "sourceRefs": ["quran-text"],
            }
        ],
        "sources": [
            {
                "sourceId": "quran-text",
                "kind": "quran-text",
                "role": "primary-ground",
                "path": "quran-data/data/text/quran-uthmani.tsv",
                "format": "tsv",
                "content": "ONLY_INLINED_CONTENT",
            }
        ],
        "coverage": {
            name: {
                "status": "complete" if name == "quranText" else "absent",
                "required": name in {"quranText", "layer2"},
                "sourceIds": ["quran-text"] if name == "quranText" else [],
                "missing": [],
                "notes": [],
            }
            for name in ("quranText", "layer2", "networkV3", "v12", "v11")
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

    assert "ONLY_INLINED_CONTENT" in prompt
    assert "<BEGIN_SOURCE_PACKET_JSON>" in prompt
    assert "<END_SOURCE_PACKET_JSON>" in prompt
    assert "Paths inside the packet are provenance labels" in prompt
