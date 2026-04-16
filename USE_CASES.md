# 🛠️ MCP Server Use Cases

The Homelab MCP Server acts as a documentation and discovery layer between your infrastructure and your LLM client. Its value is not just "chatting with servers" but turning live infrastructure state into usable documentation, audits, and troubleshooting context.

## 1. Automated Network State Regeneration

Whenever a change is made to your firewall rules, a new virtual machine is spun up, or a container service is deployed, the MCP Server is invoked to update the markdown master lists in your documentation vault (e.g., an Obsidian vault or standard Markdown wiki).

* **Firewall Rules**: Fetches firewall states to automatically update a [`Network_Master_Map.md`](./docs/examples/Network_Master_Map_Mock.md).
* **Container Mapping**: Iterates through container endpoints to rapidly rebuild a [`Container_Infrastructure_Map.md`](./docs/examples/Container_Infrastructure_Map_Mock.md).
* **Host Registry**: Parses interface configurations across virtualization nodes to keep a [`Master_Host_List.md`](./docs/examples/Master_Host_List_Mock.md) up-to-date with current IPs and MACs.
* **Proxy Routing**: Pulls dynamic configuration files from reverse proxies (e.g., Traefik/Caddy/Nginx) to chart reverse proxy routes.

## 2. Infrastructure State Capture (Cutover Reports)

Before and after maintenance windows, the MCP server is used to generate **Cutover Reports**.
These reports capture the delta between the pre-maintenance and post-maintenance states, writing them securely to the [`docs/Cutover_Report_*.md`](./docs/examples/Cutover_Report_Mock.md) logs. This ensures a strict audit trail of all manual and automated infrastructure changes.

## 3. Proactive Security Auditing

By connecting to your firewall/router API via a secured VPN interface (e.g., Tailscale / WireGuard at `<VPN_IP>`), the server enables rapid security audits.
* Validates that specific firewall aliases/groups are correctly populated.
* Backs up the full firewall XML/JSON configuration to ensure disaster recovery readiness.
* Evaluates QoS parameters to ensure bandwidth allocation is active and correctly prioritized.

## 4. Disaster Recovery Preparation

In the event of a Management Jump-Host or MCP server rebuild, this toolset provides an immediate "sanity check" loop:
* Validating secure VPN (e.g., Tailscale / WireGuard) connectivity to your firewall natively.
* Verifying container orchestrator API keys and endpoint reachability.
* Testing the SSH jump paths via the management jump-host IP to internal nodes (e.g., `user@<Internal_IP>`) before attempting large-scale deployment or monitoring loops.

## 5. Interactive, Natural Language Troubleshooting

Beyond just rendering static markdown files, an MCP server bridges the gap between your Homelab and Large Language Models (like Claude). This allows you to execute complex debugging workflows using plain English:

* **Example 1: Cross-System Correlation**
  You can ask, *"Why can't I reach the Nginx container on my DMZ?"* 
  The server dynamically queries your orchestrator API for container status, checks your virtual machine interfaces, and pulls live firewall routing to pinpoint the exact broken link—without you ever opening a terminal.

* **Example 2: Rapid Log & Metric Analysis**
  Instead of manually SSHing into your reverse proxy node to `grep` logs, you can ask, *"Are there any critical 502 Bad Gateway errors in the proxy traffic over the last 15 minutes?"* 
  The MCP server directly queries your observability stack (e.g., Loki, Prometheus, or direct container logs) and automatically summarizes the root cause of the connectivity drop.

## Choosing A Starter From These Use Cases

- If your first goal is to understand MCP structure, start with [python-minimal](./templates/python-minimal/README.md).
- If your first goal is firewall discovery or perimeter documentation, start with [python-opnsense](./templates/python-opnsense/README.md).
- If your first goal is VM/container inventory and service placement, start with [python-proxmox-portainer](./templates/python-proxmox-portainer/README.md).
- If your first goal is logs, metrics, and service-health visibility, start with [python-observability](./templates/python-observability/README.md).

## 6. Infrastructure Drift Detection (CI/CD)

An MCP Server can be integrated into GitHub Actions, GitLab CI, or a local cron job to proactively ping your infrastructure on a schedule. It compares the live state of your firewall rules and containers against your committed Markdown documents. If a manual change was made in the UI and not documented, the server flags the "drift" and can automatically generate an alert or pull request!

## 7. Dynamic Configuration Management Parsing (Ansible)

Instead of hardcoding IPs or blindly hoping an LLM guesses what virtual machines exist on a network, an MCP server can be built to actively read Infrastructure-as-Code (IaC) state files. 

For example, by equipping the server with a tool that strictly parses your local `ansible/inventory.ini` or `inventory.yaml` files, the LLM instantly knows every Hostname, Group, and IP address in your architecture. This creates an incredibly powerful self-discovery loop without you needing to explicitly prompt the AI with context!
