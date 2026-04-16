# Python Proxmox + Portainer MCP Starter

This starter is for users who want to begin with virtualization and container discovery instead of firewall discovery.

It stays read-only by default and uses exported sample data so it is safe to run before you connect it to live infrastructure.

## Environment Note

The command examples in this starter were written around Linux environments, especially Debian and Ubuntu. If your environment differs, you may need to adjust Python paths, virtual environment commands, package installation steps, or client config paths.

## What This Starter Demonstrates

- how to summarize Proxmox guests from exported JSON
- how to summarize Portainer containers from exported JSON
- how to render simple markdown inventory output
- how to model a VM/container-first MCP workflow

## Quick Start

### 1. Install dependencies

Using `uv`:

```bash
cd templates/python-proxmox-portainer
uv sync
```

Using `pip`:

```bash
cd templates/python-proxmox-portainer
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
python -m homelab_mcp_proxmox_portainer.server
```

Or:

```bash
uv run mcp run src/homelab_mcp_proxmox_portainer/server.py
```

### 4. Install into a client

```bash
uv run mcp install src/homelab_mcp_proxmox_portainer/server.py -f .env --name "Proxmox Portainer Starter"
```

## Example Read-Only Tools

- `platform_server_info`
- `proxmox_guest_summary`
- `portainer_container_summary`
- `render_platform_markdown`

## Suggested Migration To Live APIs

Once the exported-data version works:

1. replace the local JSON readers with real Proxmox and Portainer API clients
2. keep the MCP tools read-only
3. use dedicated low-privilege API tokens
4. add timeouts and rate limits
5. only add restart/redeploy tools later with human approval
