# Python OPNsense MCP Starter

This is a more opinionated Python MCP starter for users who want to begin with an OPNsense-centered homelab workflow.

It stays read-only by default and uses exported sample data so the starter is safe to run before you connect it to a live firewall.

## Environment Note

The command examples in this starter were written around Linux environments, especially Debian and Ubuntu. If your environment differs, you may need to adjust Python paths, virtual environment commands, package installation steps, or client config paths.

## What This Starter Demonstrates

- how to structure an OPNsense-oriented MCP server
- how to summarize firewall aliases and rules from exported JSON
- how to render markdown from discovered firewall data
- how to keep the first version read-only before moving to live APIs

## Quick Start

### 1. Install dependencies

Using `uv`:

```bash
cd templates/python-opnsense
uv sync
```

Using `pip`:

```bash
cd templates/python-opnsense
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
```

### 2. Create your environment file

```bash
cp .env.example .env
```

### 3. Run the server

```bash
python -m homelab_mcp_opnsense.server
```

Or:

```bash
uv run mcp run src/homelab_mcp_opnsense/server.py
```

### 4. Install into a client

```bash
uv run mcp install src/homelab_mcp_opnsense/server.py -f .env --name "OPNsense Starter"
```

## Example Read-Only Tools

- `opnsense_server_info`
- `opnsense_rule_summary`
- `opnsense_alias_summary`
- `render_firewall_markdown`

## Suggested Migration To Live APIs

Once the local exported-data version works:

1. replace the local JSON readers with a real OPNsense API client
2. keep the MCP tools read-only
3. use dedicated read-only OPNsense credentials
4. add strict timeouts and error handling
5. only add state-changing tools later with explicit human approval
