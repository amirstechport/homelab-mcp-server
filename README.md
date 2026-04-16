# Homelab MCP Server

The **Homelab MCP Server** is a public reference project for building MCP-powered homelab discovery, documentation, and audit workflows.

It is designed to show how a custom MCP server can sit between Large Language Models and infrastructure systems like OPNsense, Proxmox, Portainer, and reverse proxies while staying grounded in read-only discovery and strong safety controls.

This repo is intentionally structured as:

- a practical explanation of the use case
- a deployment and safety guide
- a set of reusable Python starter templates
- example markdown outputs and topology artifacts

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

## Validation Note

The minimal starter was validated on April 15, 2026 on a small Ubuntu 22.04 VM with 2 vCPUs, about 4 GB RAM, and about 27 GB free disk using a user-space `uv` install plus Python 3.11. The published flow worked for a basic MCP smoke test, including a real client session that listed tools and called the sample read-only tools successfully.

That size is good enough for basic starter validation, but it is not ideal for heavier local agent workflows or multiple services at once.

## Start Here

If you are new to the repo, use this path:

1. Read [USE_CASES.md](./USE_CASES.md) to understand what the MCP server is meant to do.
2. Read [SECURITY.md](./SECURITY.md) before connecting any real infrastructure.
3. Read [DEPLOYMENT.md](./DEPLOYMENT.md) to choose a safe deployment model.
4. Use [templates/README.md](./templates/README.md) to choose the right starter.

## 🏗️ Architecture & Topology

- **Firewall**: e.g., OPNsense / pfSense / Unifi (Management via secure VPN like Tailscale / WireGuard)
- **Jump-Host Security**: A Management Jump-Host acts as the exclusive gateway to internal compute nodes.
- **Compute Cluster**: Multiple virtualization nodes (e.g., Proxmox / ESXi)
- **Container Control Plane**: Container orchestrator instance (e.g., Portainer)

## ⚙️ Core Capabilities

This server is equipped with a suite of tools for deep infrastructure discovery:

1. **Firewall Perimeter Audit**: Extracts filter rules, NAT rules, aliases, and backup configurations directly from your firewall's REST API over a secure VPN (e.g., Tailscale / WireGuard).
2. **Virtualization Discovery**: SSHes via the management jump-host to map VM/container networks, interfaces, and MAC addresses.
3. **Container Mapping**: Iterates across distinct active environment endpoints to map running container services.
4. **Reverse Proxy Discovery**: Connects to nodes running your reverse proxies (e.g., Traefik, Caddy, Nginx Proxy Manager) to pull live routing configurations.
5. **Traffic & Observability**: Integrates with monitoring stacks (e.g., Prometheus, Grafana, Loki, Uptime Kuma).
6. **Infrastructure-as-Code Parsing**: Dynamically reads configuration files (e.g., Ansible `inventory.ini`) to map hosts, groups, and IP addresses without relying on hardcoded context.

## What This Repo Is Not

- not a dump of a private production homelab
- not a recommendation to give an LLM unrestricted infrastructure access
- not a fully packaged one-click product

It is a public-safe reference implementation and starter-kit repo.

## 📚 Documentation Index

To see exactly what this server can do and how to run it safely, dive into the core documentation:
* [**Use Cases & Feature Highlights**](./USE_CASES.md) - Deep dive into 7 real-world scenarios (including Interactive Troubleshooting and CI/CD Drift Detection).
* [**Deployment & Network Placement Guide**](./DEPLOYMENT.md) - Step-by-step instructions on setting up the server locally or tunneling it securely over SSH.
* [**Security & Safety Guidelines**](./SECURITY.md) - **Mandatory reading.** How to safely implement "Dry-Run" constraints and Read-Only API tokens to prevent hallucinated data destruction.
* [**Example Mockups (docs/examples/)**](./docs/examples/) - See exactly what the AI-generated Network Maps, Container Inventories, and Cutover Reports look like!
* [**Template Index**](./templates/README.md) - Choose the right starter based on whether you want a minimal, OPNsense-first, or Proxmox/Portainer-first MCP server.

## 🧰 Starter Templates

If you want to build your own MCP server instead of just reading the concept docs, start here:

* [**Template Index**](./templates/README.md) - Start here if you want help deciding which starter fits your use case.
* [**Python Minimal MCP Starter**](./templates/python-minimal/README.md) - A runnable Python starter using the official MCP Python SDK, env example, sample data, and read-only homelab-style tools.
* [**Python OPNsense MCP Starter**](./templates/python-opnsense/README.md) - A firewall-first starter focused on read-only OPNsense rule and alias discovery from exported data.
* [**Python Proxmox + Portainer MCP Starter**](./templates/python-proxmox-portainer/README.md) - A virtualization/container-first starter for Proxmox guest inventory and Portainer container discovery.
* [**Python Observability MCP Starter**](./templates/python-observability/README.md) - An observability-first starter for metrics, logs, and service-health summaries.

These starters are meant to be the copy-and-adapt path for users who want to wire in their own OPNsense, Proxmox, Portainer, Traefik, or Caddy environment later.

## 🤖 MCP Client Options

Your MCP server needs a host application that can connect to it. Good options include:

* **Claude Desktop** - A simple local MCP entry point for people who want desktop chat plus tools.
* **Claude Code** - Best when you want repo-aware coding and MCP tools in the same workflow.
* **Codex CLI / Codex IDE extension** - Good if you want OpenAI-powered coding workflows with MCP access in terminal or editor.
* **VS Code with GitHub Copilot Agent mode** - Useful if your team already works inside VS Code and wants MCP servers available there.
* **Google Antigravity** - A good fit if you want an agent-first editor that can connect to MCP servers.

The exact model you use depends on the client and your plan. A simple rule is:

* use the strongest coding-capable model available in your chosen client for implementation tasks
* use a cheaper/faster model for routine documentation refreshes or inventory reads
* keep infrastructure tools read-only regardless of which model is attached

## 🚀 Setup & Deployment

Because this server requires high-level API credentials to your core infrastructure, **where** you host this server (e.g., locally over a VPN vs. an Always-on internal Jump-Host) is a critical security decision.

Please read the complete [**Deployment & Network Placement Guide**](./DEPLOYMENT.md) for step-by-step setup instructions and architectural teardowns.

## ⚠️ Disclaimer & Safety Guidelines

**WARNING**: Giving an LLM agent access to your core infrastructure APIs and SSH jump-hosts carries massive risks. If an LLM misinterprets a prompt or hallucinates a command, it could accidentally perform destructive actions.

Please treat this repository purely as an **educational example** and read our full [**Security & Safety Guidelines (SECURITY.md)**](./SECURITY.md) before exposing your homelab.

The core tenets of MCP safety include:
* **Read-Only Credentials**: Always issue strictly scoped, read-only API tokens.
* **Require Human Approvals**: For any tool that modifies state (e.g., spinning down a container or changing a firewall rule), implement a strict "dry-run" or manual approval confirmation prompt in the MCP tool logic.
* **Beware of Data Deletion**: Never provide an MCP tool with raw `rm -rf` SSH capabilities or raw SQL `DROP` commands without extensive constraints. A misunderstanding could result in wiping an entire Proxmox node or dropping your Nextcloud database.
* **Rate Limiting**: Ensure your tools have timeouts and rate limits to prevent an LLM from accidentally getting stuck in a loop and DDoSing your own firewall API.

---
*For detailed scenarios on how this server updates the "Network Pulse" documentation and performs audits, refer to [USE_CASES.md](./USE_CASES.md).*
