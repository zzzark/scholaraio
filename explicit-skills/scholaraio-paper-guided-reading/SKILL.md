---
name: scholaraio-paper-guided-reading
description: Use when the user explicitly asks for ScholarAIO guided paper reading or invokes /scholaraio:paper-guided-reading, scholaraio-paper-guided-reading, or ScholarAIO deep reading. Do not use for generic PDF, paper, or reading requests.
---

# ScholarAIO Guided Paper Reading

Explicit-only skill. Use this skill only when the user explicitly names ScholarAIO, the `scholaraio` CLI, `/scholaraio:paper-guided-reading`, `scholaraio-paper-guided-reading`, or ScholarAIO deep reading.

If the request only asks for paper reading, PDF summary, literature review, or research help without naming ScholarAIO, stop using this skill and continue with normal tools.

## Workflow

1. Search local ScholarAIO candidates from the user's fuzzy topic, title, author, DOI, or research question.
2. Show 3-5 candidates with title, authors, year, venue, and abstract signal.
3. Ask the user to choose a target paper and clarify the reading focus.
4. Load the selected paper with `scholaraio show`, starting from L2 or L3 and using L4 only when needed.
5. Answer conversationally with evidence from the paper, figures, formulas, or sections.

## Commands

```bash
scholaraio usearch "<topic>" --limit 10
scholaraio search "<keywords>" --limit 10
scholaraio search-author "<author>" --limit 10
scholaraio show "<paper-id>" --layer 2
scholaraio show "<paper-id>" --layer 3
scholaraio show "<paper-id>" --layer 4
```

## Reading Focus

Prioritize the user's stated interest. If none is given, cover the core question, method, main findings, limitations, and how the paper relates to the user's research.

Treat conclusions as author claims, not facts. Point out weak evidence, overclaiming, missing controls, and conflicts with related papers when visible from the ScholarAIO library.

## Persistence

Do not append persistent notes unless the user asks for notes or ongoing ScholarAIO memory. When notes are requested, use a dated heading and keep them brief.
