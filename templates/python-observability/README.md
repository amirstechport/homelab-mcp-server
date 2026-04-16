# Python Observability MCP Starter

This starter is for users who want to begin with logs, metrics, and service health instead of firewall or inventory discovery.

It stays read-only by default and uses exported sample data so it is safe to run before you connect it to live monitoring systems.

## Environment Note

The command examples in this starter were written around Linux environments, especially Debian and Ubuntu. If your environment differs, you may need to adjust Python paths, virtual environment commands, package installation steps, or client config paths.

## What This Starter Demonstrates

- how to summarize Prometheus-style metric snapshots
- how to summarize Loki-style log events
- how to summarize uptime monitor state
- how to render markdown from observability data

## Quick Start

### 1. Install dependencies

Using `uv`:

```bash
cd templates/python-observability
uv sync
```

Using `pip`:

```bash
cd templates/python-observability
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
python -m homelab_mcp_observability.server
```

Or:

```bash
uv run mcp run src/homelab_mcp_observability/server.py
```

### 4. Install into a client

```bash
uv run mcp install src/homelab_mcp_observability/server.py -f .env --name "Observability Starter"
```

## Example Read-Only Tools

- `observability_server_info`
- `metrics_summary`
- `log_summary`
- `monitor_summary`
- `render_observability_markdown`

## Suggested Migration To Live APIs

Once the exported-data version works:

1. replace local JSON readers with Prometheus, Loki, or monitor API clients
2. keep the MCP tools read-only
3. add timeouts, limits, and query guards
4. expose narrow summaries before exposing free-form querying
