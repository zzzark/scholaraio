---
name: scholaraio-show
description: Use when the user explicitly asks for ScholarAIO paper reading or invokes /scholaraio:show, scholaraio-show, or scholaraio show. Do not use for generic PDF, paper, or reading requests.
---

# ScholarAIO Show

Explicit-only skill. Use this skill only when the user explicitly names ScholarAIO, the `scholaraio` CLI, `/scholaraio:show`, `scholaraio-show`, or `scholaraio show`.

If the request only says to read a PDF, summarize a paper, inspect metadata, or show an abstract without naming ScholarAIO, stop using this skill and continue with normal tools.

## Workflow

1. Identify the paper ID, directory name, UUID, DOI, or title fragment.
2. If the target is ambiguous, use ScholarAIO search first and ask the user to choose.
3. Select the smallest useful layer.
4. Summarize with evidence and mention when full text, figures, or conclusions are unavailable.

## Layers

| Layer | Command | Content |
|------|---------|---------|
| L1 | `scholaraio show "<paper-id>" --layer 1` | metadata |
| L2 | `scholaraio show "<paper-id>" --layer 2` | metadata and abstract |
| L3 | `scholaraio show "<paper-id>" --layer 3` | conclusion when enriched |
| L4 | `scholaraio show "<paper-id>" --layer 4` | full Markdown text |

For long L4 output, start with a focused excerpt or structured summary and ask before expanding.

## Notes

If the command shows existing `notes.md`, reuse it before reanalyzing the paper. Add notes only when the user explicitly wants persistent ScholarAIO notes.
