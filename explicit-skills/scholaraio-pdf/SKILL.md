---
name: scholaraio-pdf
description: Use when the user explicitly asks ScholarAIO to ingest, attach, import, or read a local PDF file, including a survey paper PDF. Do not use for generic PDF, paper, or reading requests.
---

# ScholarAIO PDF

Explicit-only skill. Use this skill only when the user explicitly names ScholarAIO, the `scholaraio` CLI, `/scholaraio:pdf`, `scholaraio-pdf`, or asks to use ScholarAIO on a local PDF file.

If the request only says to read, summarize, inspect, or analyze a PDF without naming ScholarAIO, stop using this skill and continue with normal tools.

## Workflow

1. Identify whether the PDF is a new standalone paper, a PDF for an existing ScholarAIO record, or a file that should stay outside the library.
2. For a new standalone paper or survey PDF, place it in the right ScholarAIO inbox and run an ingest preview first.
3. For an existing paper record, use `attach-pdf` and confirm before replacing any existing canonical PDF.
4. After ingest or attach succeeds, use `scholaraio-show` or `scholaraio-paper-guided-reading` for reading.
5. Report the paper ID, generated Markdown status, and any missing conversion or metadata issues.

## Commands

```bash
scholaraio pipeline ingest --dry-run
scholaraio pipeline ingest --inspect
scholaraio attach-pdf "<paper-id>" "<path-to-paper.pdf>"
scholaraio attach-pdf "<paper-id>" "<path-to-paper.pdf>" --force
scholaraio show "<paper-id>" --layer 2
scholaraio show "<paper-id>" --layer 4
```

Use `--force` only after explicit confirmation, because it can replace an existing canonical PDF.

## Inbox Routing

| PDF kind | Inbox |
|---------|-------|
| ordinary paper or survey paper | `data/spool/inbox/` |
| thesis | `data/spool/inbox-thesis/` |
| patent | `data/spool/inbox-patent/` |
| technical report or non-paper document | `data/spool/inbox-doc/` |
| proceedings volume | `data/spool/inbox-proceedings/` |

## Reading Survey Papers

For survey papers, start with L2 metadata and abstract, then L4 full text. Extract the taxonomy, coverage boundary, comparison criteria, main tables, claimed gaps, and dated assumptions. Treat all survey claims as author interpretations unless backed by cited evidence.

## Safety

This skill can write to the ScholarAIO library and indexes. Ask before running write actions unless the user explicitly requested the action in the current message.
