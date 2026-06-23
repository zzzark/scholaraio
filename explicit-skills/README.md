# ScholarAIO Explicit Skills

This directory contains explicit-only wrappers for daily global agent use.

The main `.claude/skills/` directory keeps ScholarAIO's broad project skills with generic names such as `search`, `show`, and `explore`. Those are useful when working inside the ScholarAIO repository or plugin namespace, but they can be too broad as global skills.

Install these wrappers instead when ScholarAIO should activate only after the user explicitly names ScholarAIO, `/scholaraio:*`, or the prefixed skill name.

## Included Skills

- `scholaraio-search`
- `scholaraio-show`
- `scholaraio-paper-guided-reading`
- `scholaraio-ingest`
- `scholaraio-explore`

## Manual Install

Copy the selected directories into the agent's personal skills directory, for example:

```powershell
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.agents\skills"
Copy-Item -Recurse -Force ".\explicit-skills\scholaraio-*" "$env:USERPROFILE\.agents\skills\"
```

Restart the agent after installation so the skill list refreshes.
