# 🧠 MCP Server Deployment & Network Placement

When adding an AI-driven automation engine to your homelab, **where** you place the server is just as important as the code it runs. 

Because the MCP server requires high-level API access to your Firewall, Proxmox nodes, and Portainer instances, you have two primary deployment architectures to choose from depending on your security tolerance:

## Recommended Reading Order

1. [Security & Safety Guidelines](./SECURITY.md)
2. [Template Index](./templates/README.md)
3. The architecture choice below
4. The starter setup steps in this file

## Environment Compatibility Note

The setup commands in this repo were shaped around Linux systems, especially Debian and Ubuntu servers. Treat them as a strong baseline rather than a guaranteed copy-paste setup for every environment.

If you are on macOS, Windows, or a different Linux distribution, you may need to adjust:

- Python interpreter paths
- virtual environment activation steps
- package-manager commands
- shell syntax
- MCP client configuration file locations

## System Requirements

### Minimum

- Python `3.11+`
- `venv` + `pip`, or `uv`
- an MCP-capable client
- 2 CPU cores
- 4 GB RAM
- about 1 GB free disk space

### Recommended

- Debian or Ubuntu Linux environment
- `uv`
- read-only API credentials for any live systems you want to query
- SSH access to a jump host if your architecture requires one
- 4+ CPU cores
- 8 GB RAM or more
- about 5 GB free disk space if you plan to keep multiple virtual environments, exported artifacts, and diagrams

---

## Architecture 1: The "Remote Admin" Model (Recommended for Beginners)
**Location:** Your personal Desktop/Laptop running the Claude Desktop Client.
**Network Flow:** Laptop ➔ Tailscale / WireGuard ➔ Homelab APIs

In this model, the MCP Server code runs locally on your laptop. When you open Claude and ask a question, the local MCP server executes the command and tunnels through your secure VPN to reach the homelab's management VLAN.

* **Pros:** 
  * Extreme security: If your laptop is off or disconnected from the VPN, the MCP server has zero access to your network.
  * No exposed internal listeners or open ports on your network.
  * Easiest to develop, debug, and configure.
* **Cons:** 
  * You cannot run automated overnight "Drift Detection" cron jobs because the server relies on your laptop being alive.

## Architecture 2: The "Always-On Jump-Host" Model
**Location:** An isolated Management Server or Ansible VM inside your Homelab.
**Network Flow:** Isolated Management VLAN ➔ Cloud AI API (e.g., Anthropic) ➔ Specific Homelab APIS

In this model, the MCP server runs as a background service (e.g., `systemd` or Docker) on a dedicated, highly locked-down "Jump-Host" virtual machine inside your network. 

* **Pros:** 
  * Always online, making it perfect for CI/CD, scheduled drift detection, and daily cutover reports.
  * Allows you to query your homelab from your phone or external devices without needing the Claude Desktop app running locally.
* **Cons:** 
  * **High Security Risk:** If this VM is ever breached, the attacker gains the API keys to your firewall and hypervisors. 
  * Requires strict firewall rules ensuring this VM can only talk to specific management IPs and nowhere else.

---

## 🚀 Step-by-Step Setup Guide

Regardless of which architecture you chose, the setup procedure is the same:

### 1. Configure the Environment
Clone the repository and inject your API credentials.
```bash
git clone https://github.com/amirstechport/homelab-mcp-server.git
cd homelab-mcp-server
```

If you want a runnable starter instead of building from scratch, use:

```bash
cd templates/python-minimal
cp .env.example .env
```

Or start from the firewall-focused template:

```bash
cd templates/python-opnsense
cp .env.example .env
```

Or start from the virtualization/container template:

```bash
cd templates/python-proxmox-portainer
cp .env.example .env
```

Or start from the observability template:

```bash
cd templates/python-observability
cp .env.example .env
```

If you are unsure which one to choose, use the template chooser:

- [Template Index](./templates/README.md)

### 2. Install Dependencies
The reusable starters in this repo are Python-based:
```bash
cd templates/python-minimal

# With uv
uv sync

# Or with pip
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
```

### 3. Connect to your MCP Client
You need to register the server with your LLM Client (e.g., Claude Desktop or Google Antigravity).

**Option A: Running Locally**
If you cloned one of the Python starters directly to your laptop, configure your client to run the starter with `uv`:

```json
{
  "mcpServers": {
    "homelab-server-local": {
      "command": "uv",
      "args": [
        "run",
        "mcp",
        "run",
        "/absolute/path/to/your/homelab-mcp-server/templates/python-minimal/src/homelab_mcp_starter/server.py"
      ]
    }
  }
}
```

**Option B: The "Remote Execution" Model (Running over SSH)**
If you prefer to keep the MCP code physically hosted on your Homelab Jump-Host but want to access it securely from your local laptop's LLM Client, you can use `ssh` as the execution command! The client will seamlessly tunnel the standard input/output over SSH.

```json
{
  "mcpServers": {
    "homelab-server-remote": {
      "command": "ssh",
      "args": [
        "-i",
        "/path/to/your/private/key/.ssh/id_ed25519",
        "user@<Jump_Host_IP>",
        "cd /path/to/remote/homelab-mcp-server/templates/python-minimal && /path/to/remote/.local/bin/uv run mcp run src/homelab_mcp_starter/server.py"
      ]
    }
  }
}
```

### 4. Restart your Client
Completely quit and restart your Claude Desktop application. You should now see the `homelab-server` tools available in your UI (often denoted by a small hammer icon)!

---

## Recommended MCP Clients

These are good places to attach your MCP server:

* **Claude Desktop** - Easiest for desktop chat + MCP tools.
* **Claude Code** - Best when you want MCP tools available alongside code editing and repo work.
* **Codex CLI / Codex IDE extension** - Good for OpenAI-based coding workflows with MCP access.
* **VS Code with GitHub Copilot Agent mode** - Useful for teams already standardizing on VS Code.
* **Google Antigravity** - Good for users who want an agent-style editor with MCP support.

## Practical Model Guidance

The client application and your plan determine which exact model names are available, so this repo avoids hardcoding a single required model. A safe recommendation is:

* use the strongest coding-oriented model available in your chosen client for MCP server development
* use a cheaper or faster model for routine inventory reads and documentation refreshes
* keep infrastructure-facing MCP tools read-only even when using the strongest model
