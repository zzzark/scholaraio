---
name: scholaraio-ingest
description: Use when the user explicitly asks for ScholarAIO ingest or invokes /scholaraio:ingest, scholaraio-ingest, or scholaraio pipeline. Do not use for generic PDF or document processing requests.
---

# ScholarAIO Ingest

Explicit-only skill. Use this skill only when the user explicitly names ScholarAIO, the `scholaraio` CLI, `/scholaraio:ingest`, `scholaraio-ingest`, `scholaraio ingest`, or `scholaraio pipeline`.

If the request only asks to process, convert, summarize, or read PDFs without naming ScholarAIO, stop using this skill and continue with normal tools.

## Workflow

1. Confirm which ScholarAIO inbox or source the user wants to process.
2. Preview with `--dry-run` or `--inspect` when the action could write files or change indexes.
3. Use the narrowest preset that matches the request.
4. Report created records, pending records, failures, and any follow-up command needed.

## Inbox Paths

| Input | Normal path |
|------|-------------|
| papers | `data/spool/inbox/` |
| theses | `data/spool/inbox-thesis/` |
| patents | `data/spool/inbox-patent/` |
| Office and general docs | `data/spool/inbox-doc/` |
| proceedings | `data/spool/inbox-proceedings/` |

## Commands

```bash
scholaraio pipeline ingest --dry-run
scholaraio pipeline ingest --inspect
scholaraio pipeline full --inspect
scholaraio pipeline reindex
scholaraio ingest-link "<url>"
scholaraio fetch-pdf "<doi-or-url>" --direct
```

Use `fetch-pdf --direct` only for the user's legitimate network access context. Do not imply access bypassing.

Proceedings are semi-automatic: run ingest first, review generated candidates, then apply split or clean plans only after explicit confirmation.

## Safety

This skill can write to the ScholarAIO library and indexes. Ask before running write actions unless the user already gave a clear apply instruction in the current message.
