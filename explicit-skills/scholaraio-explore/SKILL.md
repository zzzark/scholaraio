---
name: scholaraio-explore
description: Use when the user explicitly asks for ScholarAIO exploration or invokes /scholaraio:explore, scholaraio-explore, or scholaraio explore. Do not use for generic research or web exploration requests.
---

# ScholarAIO Explore

Explicit-only skill. Use this skill only when the user explicitly names ScholarAIO, the `scholaraio` CLI, `/scholaraio:explore`, `scholaraio-explore`, or `scholaraio explore`.

If the request only asks to explore a topic, survey a field, search the web, or review literature without naming ScholarAIO, stop using this skill and continue with normal tools.

## Workflow

1. Identify whether the user wants to fetch a new explore library, search an existing explore library, list libraries, build embeddings, cluster topics, or create visualizations.
2. Ask before fetching external records or building indexes when the user has not already authorized it.
3. Keep explore libraries isolated from the main ScholarAIO paper library.
4. Report library name, source filter, record count, and next useful command.

## Commands

```bash
scholaraio explore list
scholaraio explore info
scholaraio explore info --name "<name>"
scholaraio explore search --name "<name>" "<query>" --limit 10
scholaraio explore search --name "<name>" "<query>" --mode keyword --limit 10
scholaraio explore search --name "<name>" "<query>" --mode unified --limit 10
scholaraio explore fetch --keyword "<topic>" --name "<name>"
scholaraio explore fetch --issn "<issn>" --name "<name>"
scholaraio explore embed --name "<name>"
scholaraio explore topics --name "<name>" --build
scholaraio explore viz --name "<name>"
```

## Fetch Filters

Use OpenAlex filters the user provides: ISSN, concept ID, topic ID, author ID, institution ID, keyword, source type, open-access type, citation count, and year range.

Use stable, short library names. For repeated fetches, prefer `--incremental` when updating an existing library.

## Safety

Fetching, embedding, clustering, and visualization can write data and take time. Preview the plan and ask for confirmation unless the user explicitly requested the action.
