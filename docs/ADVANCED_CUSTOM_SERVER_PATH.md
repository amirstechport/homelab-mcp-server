# 🛠️ Advanced Custom Server Path

Use this path if you already know you want to build your own MCP server around your own infrastructure.

## Best Fit

This path is for you if:

- sample-data testing is not enough
- you want your own firewall, virtualization, proxy, or observability integrations
- you want your own output format and documentation workflow

## Recommended Order

1. Read [USE_CASES.md](../USE_CASES.md) for the kinds of workflows this repo is modeling.
2. Read [Choose a Starter](../templates/README.md) and pick the closest starter.
3. Read [DEPLOYMENT.md](../DEPLOYMENT.md) before deciding where the server should run.
4. Read [SECURITY.md](../SECURITY.md) before adding live credentials or SSH access.
5. Replace sample-data readers with your own read-only integrations.

## Repo-Level Instruction Files

Some clients support repo-level instruction files that can help keep your agent behavior narrow and predictable:

- **Claude Code:** `CLAUDE.md`
- **Codex:** `AGENTS.md`
- **Google Antigravity:** `AGENTS.md` can be a practical convention if the attached agent stack supports it

Use these files for:

- project rules
- allowed tools
- approval expectations
- safety boundaries

Do not put secrets, tokens, private IP maps, or production credentials in them.

Do not assume these files are active just because they exist in the repo.

- first confirm that your chosen client supports them
- then confirm that the running session is actually honoring them

Until then, keep the important safety rules in your active prompts too.

## Rule of Thumb

Keep your first live tools:

- read-only
- narrow in scope
- timeout-protected
- approval-driven if anything can change state

And keep your first live credentials:

- least-privilege
- read-only
- scoped as tightly as possible
