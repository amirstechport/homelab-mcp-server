# 🛡️ MCP Security & Safety Guidelines

**The Golden Rule:** You must treat Large Language Models (LLMs) as highly capable but **fully untrusted actors**. 

Giving an AI the ability to read and execute commands in your homelab carries immense risk. If an LLM misinterprets your prompt, hallucinates a command, or gets stuck in a loop, it could cause catastrophic damage to your data or infrastructure. 

This document serves as a starting point for safely designing and deploying your own MCP tools.

Before building on any starter in this repo, read this file first and keep every initial tool read-only.

---

## 1. Principle of Least Privilege (Read-Only by Default)

Never give your MCP server an admin-level API key unless absolutely necessary.
* **Proxmox:** Create a dedicated API token and assign it the `PVEAuditor` role so it can read VM states and network interfaces but cannot delete or modify them.
* **Portainer/Docker:** Issue standard-user API keys that only have access to view specific environments, or use read-only Docker socket proxies if hitting the daemon directly.
* **Firewall (OPNsense/pfSense):** Restrict the API user groups to `Diagnostics` or `Status` pages. Block all `POST/PUT/DELETE` API routes for the MCP user.

## 2. Execution Constraints & Human-in-the-Loop

If you *must* build a tool that modifies state (e.g., spinning down a container or pushing a firewall rule), you must build a safety catch:
* **The "Dry-Run" Pattern:** The MCP tool should default to a "dry-run" behavior where it simply prints out the exact command it *intends* to run. The user must then manually review it before giving the LLM a secondary approval to execute.
* **Never Expose Raw Shells:** Do not give an LLM an open `ssh_execute` tool where it can pass any arbitrary bash command. Instead, build specific tools like `restart_container(container_id)` that handle the SSH execution safely behind the scenes.

## 3. Network Isolation

* **VLAN Segmentation:** Place your MCP server (or Jump-Host) on an isolated Management VLAN. Restrict its outbound network access so it can **only** talk to the specific APIs it needs (e.g., Portainer on port `9443`, OPNsense on port `44334`).
* **Zero-Trust Tunnels:** If querying from a local laptop, use Tailscale or WireGuard ACLs to ensure the laptop can only hit the MCP server and not the broader infrastructure.

## 4. Rate Limiting & Timeouts

LLMs can sometimes get confused, hallucinate loops, or repeatedly call the same tool if they don't get the answer they expect.
* **Timeouts:** Ensure every HTTP request in your MCP server code has a strict timeout (e.g., 5 seconds) so it doesn't hang the client.
* **Rate Limits:** Implement basic memory rate-limiting in your tool logic so the LLM cannot spam your firewall API 50 times a second and accidentally DDoS your own network.

---
*Stay paranoid, stay secure, and happy automating.*
