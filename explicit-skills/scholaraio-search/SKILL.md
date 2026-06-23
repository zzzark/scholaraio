---
name: scholaraio-search
description: Use when the user explicitly asks for ScholarAIO search or invokes /scholaraio:search, scholaraio-search, or scholaraio search. Do not use for generic search, PDF, paper, or reading requests.
---

# ScholarAIO Search

Explicit-only skill. Use this skill only when the user explicitly names ScholarAIO, the `scholaraio` CLI, `/scholaraio:search`, `scholaraio-search`, or `scholaraio search`.

If the request only says to search, find papers, read PDFs, review literature, or explore a topic without naming ScholarAIO, stop using this skill and continue with normal tools.

## Workflow

1. Parse the query, limits, year filters, journal filters, type filters, and whether the user wants keyword, semantic, chunk, author, or federated search.
2. Prefer unified local-library search unless the user asked for a specific mode.
3. Present concise results with paper ID, title, authors, year, venue, and why each result matches.
4. Ask before fetching external sources, downloading PDFs, or modifying the library.

## Commands

```bash
scholaraio usearch "<query>" --limit 10
scholaraio search "<query>" --limit 10
scholaraio vsearch "<query>" --limit 10
scholaraio search --chunk "<query>" --limit 10
scholaraio search-author "<author>" --limit 10
scholaraio fsearch "<query>" --scope main,arxiv --limit 10
```

Use `--year`, `--journal`, and `--type` when the user gives constraints. Put years in `--year` and authors in `search-author`; do not pack author, year, and topic into one noisy query.

## Safety

This skill reads or searches ScholarAIO data. It must not create new libraries, fetch PDFs, or ingest files unless the user explicitly asks for that action.
