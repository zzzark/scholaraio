from __future__ import annotations

from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
EXPLICIT_SKILLS_DIR = ROOT / "explicit-skills"
EXPECTED_SKILLS = {
    "scholaraio-search",
    "scholaraio-show",
    "scholaraio-pdf",
    "scholaraio-paper-guided-reading",
    "scholaraio-ingest",
    "scholaraio-explore",
}


def _frontmatter(path: Path) -> tuple[dict[str, str], str]:
    text = path.read_text(encoding="utf-8")
    assert text.startswith("---\n")
    _start, frontmatter, body = text.split("---\n", 2)
    data = yaml.safe_load(frontmatter)
    assert isinstance(data, dict)
    return data, body


def test_explicit_skill_bundle_contains_expected_wrappers() -> None:
    found = {path.parent.name for path in EXPLICIT_SKILLS_DIR.glob("scholaraio-*/SKILL.md")}

    assert found == EXPECTED_SKILLS


def test_explicit_skills_are_prefixed_and_opt_in_only() -> None:
    for skill_path in sorted(EXPLICIT_SKILLS_DIR.glob("scholaraio-*/SKILL.md")):
        data, body = _frontmatter(skill_path)
        name = str(data.get("name") or "")
        description = str(data.get("description") or "")

        assert name == skill_path.parent.name
        assert name.startswith("scholaraio-")
        assert description.startswith("Use when ")
        assert "explicit" in description.lower()
        assert "Do not use" in description
        assert "Explicit-only skill" in body
        assert "stop using this skill" in body
