# Homelab MCP Server

The **Homelab MCP Server** is a public reference repo for MCP-powered homelab discovery, documentation, and audit workflows.

It shows how a custom MCP server can sit between an LLM and systems like OPNsense, Proxmox, Portainer, and reverse proxies while staying grounded in read-only discovery and strong safety controls.

## What This Repo Is

- a reference repo for a real homelab MCP use case
- a set of reusable Python starter templates
- a few public-safe example outputs
- a deployment and safety guide for doing this responsibly

## Who This Is For

- people who want to try MCP against homelab-style data quickly
- people who want a starting point for OPNsense, Proxmox, Portainer, or observability workflows
- people who want a safer, read-only-first pattern instead of exposing raw infrastructure access

## 🚀 Quick Start

If you want the fastest path:

1. Read [Quick Start](./docs/QUICK_START.md).
2. Start with [python-minimal](./templates/python-minimal/README.md).
3. Run it with sample data first.
4. Read [SECURITY.md](./SECURITY.md) before wiring in any live systems.

If you want the lazy but cautious path:

1. Read [Starter Prompts](./docs/STARTER_PROMPTS.md).
2. Let your LLM scaffold a small read-only starter for you.
3. Review the code before running it.
4. Verify the server is active in your client with [Interact With Your MCP Server](./docs/INTERACT_WITH_MCP.md).

If you want a simpler path before building your own server:

1. Read [Trusted Public MCP Path](./docs/TRUSTED_PUBLIC_MCP_PATH.md).
2. Start with official MCP SDKs or reference servers.
3. Come back here when you are ready to build a custom server around your own environment.

If you want the deeper architecture and safety path:

1. Read [Advanced Custom Server Path](./docs/ADVANCED_CUSTOM_SERVER_PATH.md).
2. Read [DEPLOYMENT.md](./DEPLOYMENT.md).
3. Read [SECURITY.md](./SECURITY.md).

## Environment Notes

The command examples in this repo are intended as a working baseline, not a universal exact setup script.

They were shaped around Linux environments, especially Debian and Ubuntu systems. Depending on your OS, shell, Python installation, package manager, and MCP client, you may need to adjust:

- virtual environment commands
- Python executable paths
- `uv` or `pip` usage
- shell quoting
- local MCP client configuration paths

## System Requirements

### Minimum

- Python `3.11+`
- a shell environment
- `pip` with `venv`, or `uv`
- an MCP-capable client such as Claude Desktop, Claude Code, Codex, VS Code, or Google Antigravity
- 2 CPU cores
- 4 GB RAM
- about 1 GB free disk space

### Recommended

- Linux environment, especially Debian or Ubuntu
- Python `3.11+` or newer
- `uv` for dependency and MCP workflow management
- network reachability to your lab systems if you plan to move beyond sample data
- read-only API credentials and, where needed, SSH access to a management jump host
- 4+ CPU cores
- 8 GB RAM or more
- about 5 GB free disk space if you plan to keep multiple virtual environments, exported artifacts, and topology assets

## Validated Starter

The minimal starter was validated on April 15, 2026 on a small Ubuntu 22.04 VM with 2 vCPUs, about 4 GB RAM, and about 27 GB free disk using a user-space `uv` install plus Python 3.11. The published flow worked for a basic MCP smoke test, including a real client session that listed tools and called the sample read-only tools successfully.

That size is good enough for basic starter validation, but it is not ideal for heavier local agent workflows or multiple services at once.

## What You Can Build

- firewall and alias summaries from OPNsense-style data
- VM and container inventory from Proxmox and Portainer-style data
- reverse proxy and service maps
- observability summaries from logs, metrics, and monitor exports
- markdown outputs for topology, host inventory, and cutover-style notes

## What This Repo Is Not

- not a dump of a private production homelab
- not a recommendation to give an LLM unrestricted infrastructure access
- not a fully packaged one-click product

It is a public-safe reference implementation and starter-kit repo.

## ✨ A Good Shortcut

If building the first version by hand feels like too much friction, a reasonable shortcut is to let your LLM scaffold a very small MCP server for you.

That can be a good onboarding move if you keep it:

- read-only
- sample-data first
- small enough to review line by line
- limited to one or two safe tools at first

Use [Starter Prompts](./docs/STARTER_PROMPTS.md) for that path, then use [Interact With Your MCP Server](./docs/INTERACT_WITH_MCP.md) to confirm the server is actually active in your client.

## 🧭 Choose Your Path

- [Quick Start](./docs/QUICK_START.md)
- [Starter Prompts](./docs/STARTER_PROMPTS.md)
- [Interact With Your MCP Server](./docs/INTERACT_WITH_MCP.md)
- [Trusted Public MCP Path](./docs/TRUSTED_PUBLIC_MCP_PATH.md)
- [Advanced Custom Server Path](./docs/ADVANCED_CUSTOM_SERVER_PATH.md)
- [Choose a Starter](./templates/README.md)
- [Deployment Guide](./DEPLOYMENT.md)
- [Security Guide](./SECURITY.md)
- [Use Cases](./USE_CASES.md)
- [Example Outputs](./docs/examples/)

## Starter Templates

If you want to build your own MCP server, start here:

* [**Choose a Starter**](./templates/README.md) - Quick path for choosing the right starting point.
* [**Python Minimal MCP Starter**](./templates/python-minimal/README.md) - A runnable Python starter using the official MCP Python SDK, env example, sample data, and read-only homelab-style tools.
* [**Python OPNsense MCP Starter**](./templates/python-opnsense/README.md) - A firewall-first starter focused on read-only OPNsense rule and alias discovery from exported data.
* [**Python Proxmox + Portainer MCP Starter**](./templates/python-proxmox-portainer/README.md) - A virtualization/container-first starter for Proxmox guest inventory and Portainer container discovery.
* [**Python Observability MCP Starter**](./templates/python-observability/README.md) - An observability-first starter for metrics, logs, and service-health summaries.

These starters are the copy-and-adapt path for users who want to wire in their own environment later.

## MCP Client Options

Your MCP server needs a host application that can connect to it. Good options include:

* **Claude Desktop** - A simple local MCP entry point for people who want desktop chat plus tools.
* **Claude Code** - Best when you want repo-aware coding and MCP tools in the same workflow.
* **Codex CLI / Codex IDE extension** - Good if you want OpenAI-powered coding workflows with MCP access in terminal or editor.
* **VS Code with GitHub Copilot Agent mode** - Useful if your team already works inside VS Code and wants MCP servers available there.
* **Google Antigravity** - A good fit if you want an agent-first editor that can connect to MCP servers.

## 🔒 Safety First

Read [SECURITY.md](./SECURITY.md) before connecting any live infrastructure. The short version:

* use read-only credentials
* do sample-data testing first
* avoid raw shell access
* require explicit approval for any state-changing action

---
*For deeper scenarios and architecture details, see [USE_CASES.md](./USE_CASES.md) and [DEPLOYMENT.md](./DEPLOYMENT.md).*
