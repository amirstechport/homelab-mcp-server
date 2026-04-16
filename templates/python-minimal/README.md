# Python Minimal MCP Starter

This is a minimal Python starter for building a homelab-oriented MCP server with the official Python SDK.

It is intentionally small:

- one FastMCP server
- read-only example tools
- simple environment variables
- no external infrastructure required to run the starter

## Environment Note

The command examples in this starter were written around Linux environments, especially Debian and Ubuntu. If your environment differs, you may need to adjust Python paths, virtual environment commands, package installation steps, or client config paths.

## Validation Note

This starter was validated on April 15, 2026 on a small Ubuntu 22.04 VM with 2 vCPUs, about 4 GB RAM, and about 27 GB free disk using a user-space `uv` install plus Python 3.11. A real MCP client session was able to connect to the starter, list tools, and call the sample read-only tools successfully.

That footprint is enough for basic starter validation, but it is not ideal for heavier local agent workflows or multiple services at once.

## What This Starter Demonstrates

- how to structure a small Python MCP server
- how to use the official `mcp[cli]` package
- how to expose read-only tools safely
- how to point the server at local exported files before wiring in live APIs

## Quick Start

### 1. Create a virtual environment and install dependencies

Using `uv`:

```bash
cd templates/python-minimal
uv sync
```

Using `pip`:

```bash
cd templates/python-minimal
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
```

### 2. Create your environment file

```bash
cp .env.example .env
```

### 3. Run the server directly

```bash
python -m homelab_mcp_starter.server
```

Or with the MCP CLI:

```bash
uv run mcp run src/homelab_mcp_starter/server.py
```

### 4. Install it into Claude Desktop

```bash
uv run mcp install src/homelab_mcp_starter/server.py -f .env --name "Homelab Starter"
```

## Example Read-Only Tools

- `starter_server_info`
  - returns basic server metadata and env-driven status
- `inventory_summary`
  - reads a local inventory export and summarizes hosts
- `proxy_route_summary`
  - reads a local JSON export of reverse-proxy routes and summarizes targets
- `render_host_markdown`
  - turns structured host input into a markdown host record

## Suggested Next Steps

Replace the local-file readers with your real integrations:

- OPNsense API
- Proxmox API
- Portainer API
- Traefik / Caddy / NPM config readers
- Obsidian or markdown-vault documentation outputs

Keep the tools read-only until you have a strong approval and dry-run pattern in place.
