from __future__ import annotations

import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def _read(rel_path: str) -> str:
    return (ROOT / rel_path).read_text(encoding="utf-8")


def _line_count(rel_path: str) -> int:
    return len(_read(rel_path).splitlines())


def test_entry_docs_stay_light_and_point_to_deep_reference() -> None:
    agents = _read("AGENTS.md")
    claude = _read("CLAUDE.md")
    agents_cn = _read("AGENTS_CN.md")

    assert "intentionally short" in agents
    assert "docs/DESIGN.md" in agents
    assert "docs/guide/agent-reference.md" in agents
    assert ".claude/skills/" in agents
    assert _line_count("AGENTS.md") < 180

    assert "intentionally stays light" in claude
    assert "docs/DESIGN.md" in claude
    assert "@AGENTS.md" in claude
    assert _line_count("CLAUDE.md") < 20

    assert "有意保持精简" in agents_cn
    assert "docs/DESIGN.md" in agents_cn
    assert "docs/guide/agent-reference.md" in agents_cn
    assert _line_count("AGENTS_CN.md") < 180


def test_repository_knowledge_system_is_indexed_for_agents() -> None:
    required_docs = (
        "docs/DESIGN.md",
        "docs/PLANS.md",
        "docs/QUALITY_SCORE.md",
        "docs/design-docs/index.md",
        "docs/product-specs/index.md",
        "docs/exec-plans/index.md",
        "docs/exec-plans/tech-debt-tracker.md",
        "docs/references/index.md",
        "docs/generated/index.md",
        "docs/validation/index.md",
    )
    for rel_path in required_docs:
        assert (ROOT / rel_path).exists(), f"{rel_path} should exist"

    design = _read("docs/DESIGN.md")
    for directory in (
        "docs/design-docs/",
        "docs/product-specs/",
        "docs/exec-plans/",
        "docs/references/",
        "docs/generated/",
        "docs/validation/",
    ):
        assert directory in design

    mkdocs = _read("mkdocs.yml")
    assert "Repository Knowledge:" in mkdocs
    assert "Knowledge Map: DESIGN.md" in mkdocs
    assert "Execution Plans: exec-plans/index.md" in mkdocs


def test_wrappers_and_setup_docs_defer_to_shared_entry_and_reference() -> None:
    for rel_path in (
        ".windsurfrules",
        ".clinerules",
        ".github/copilot-instructions.md",
        ".cursorrules",
        ".cursor/rules/scholaraio.mdc",
        ".qwen/QWEN.md",
        "docs/getting-started/agent-setup.md",
        "README.md",
        "README_CN.md",
        "docs/index.md",
    ):
        content = _read(rel_path)
        assert "agent-reference" in content.lower()


def test_agent_reference_doc_exists_and_links_core_surfaces() -> None:
    content = _read("docs/guide/agent-reference.md")

    assert ".claude/skills/" in content
    assert "docs/DESIGN.md" in content
    assert "docs/design-docs/index.md" in content
    assert "docs/exec-plans/index.md" in content
    assert "docs/exec-plans/completed/scholaraio-upgrade-plan.md" in content
    assert "docs/validation/upgrade-validation-matrix.md" in content
    assert "docs/guide/cli-reference.md" in content
    assert "workspace.yaml" in content
    assert "notes.md" in content


def test_user_and_skill_docs_do_not_claim_implicit_legacy_runtime_detection() -> None:
    stale_phrases = ("auto-detected", "自动探测", "自动识别", "自动兼容", "data/explore/<name>")
    public_docs = (
        "README.md",
        "README_CN.md",
        "docs/guide/ingestion.md",
        ".claude/skills/arxiv/SKILL.md",
        ".claude/skills/explore/SKILL.md",
        ".claude/skills/ingest/SKILL.md",
        ".claude/skills/patent-fetch/SKILL.md",
        ".claude/skills/patent-search/SKILL.md",
    )

    offenders: list[str] = []
    for rel_path in public_docs:
        content = _read(rel_path)
        for phrase in stale_phrases:
            if phrase in content:
                offenders.append(f"{rel_path}: {phrase}")

    assert not offenders, (
        "Docs should point users to migrate upgrade instead of implicit legacy runtime detection:\n"
        + "\n".join(offenders)
    )


def test_active_skills_describe_current_workspace_system_output_defaults() -> None:
    required_paths = {
        ".claude/skills/translate/SKILL.md": "workspace/_system/translation-bundles/",
        ".claude/skills/draw/SKILL.md": "workspace/_system/figures/",
        ".claude/skills/document/SKILL.md": "workspace/_system/figures/",
        "docs/guide/translate.md": "workspace/_system/translation-bundles/",
    }
    stale_paths = {
        ".claude/skills/translate/SKILL.md": ("workspace/translation-ws/",),
        ".claude/skills/draw/SKILL.md": ("workspace/figures/",),
        ".claude/skills/document/SKILL.md": ("workspace/figures/",),
        "docs/guide/translate.md": ("workspace/translation-ws/",),
    }

    failures: list[str] = []
    for rel_path, required in required_paths.items():
        content = _read(rel_path)
        if required not in content:
            failures.append(f"{rel_path}: missing {required}")
        for stale in stale_paths.get(rel_path, ()):
            if stale in content:
                failures.append(f"{rel_path}: stale {stale}")

    assert not failures, "Active skills/guides should match current workspace system-output defaults:\n" + "\n".join(
        failures
    )


def test_active_project_skill_metadata_is_trigger_focused_and_xml_safe() -> None:
    failures: list[str] = []
    for skill_path in sorted((ROOT / ".claude" / "skills").glob("*/SKILL.md")):
        if skill_path.parent.name == "_templates":
            continue
        text = skill_path.read_text(encoding="utf-8")
        assert text.startswith("---\n"), f"{skill_path} must start with YAML frontmatter"
        _, frontmatter, _body = text.split("---\n", 2)
        data = yaml.safe_load(frontmatter)
        name = data.get("name")
        description = str(data.get("description", ""))

        if name != skill_path.parent.name:
            failures.append(f"{skill_path}: name={name!r}")
        if not re.fullmatch(r"[a-z0-9-]{1,64}", str(name or "")):
            failures.append(f"{skill_path}: invalid name")
        allowed_keys = {"name", "description"}
        extra_keys = set(data) - allowed_keys
        if extra_keys:
            failures.append(f"{skill_path}: unsupported frontmatter keys {sorted(extra_keys)}")
        if not description or len(description) > 500:
            failures.append(f"{skill_path}: invalid description length {len(description)}")
        if not description.startswith("Use when "):
            failures.append(f"{skill_path}: description must start with a clear 'Use when' trigger")
        if "<" in description or ">" in description:
            failures.append(f"{skill_path}: description must not contain XML-like angle brackets")

    assert not failures, "Active project skill metadata should stay discoverable:\n" + "\n".join(failures)
