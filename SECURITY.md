# 🛡️ MCP Security & Safety Guidelines

**The Golden Rule:** You must treat Large Language Models (LLMs) as highly capable but **fully untrusted actors**. 

Giving an AI the ability to read and execute commands in your homelab carries immense risk. If an LLM misinterprets your prompt, hallucinates a command, or gets stuck in a loop, it could cause catastrophic damage to your data or infrastructure. 

This document serves as a starting point for safely designing and deploying your own MCP tools.

Before building on any starter in this repo, read this file first and keep every initial tool read-only.

## Instruction Files

If your client supports repo-level instruction files, use them to keep the agent behavior narrow and predictable:

* **Claude Code:** `CLAUDE.md`
* **Codex:** `AGENTS.md`
* **Google Antigravity:** `AGENTS.md` can be a useful convention when the attached agent stack supports it

Use these files for project rules, allowed tools, approval expectations, and safety boundaries. Do not put secrets, tokens, private IP maps, or production credentials in them.

Do not assume every client or agent surface will automatically read these files.

- verify that your client actually supports them
- verify that the active session is honoring them
- do not rely on them as your only safety control until that is confirmed

Until you have that greenlight, keep your important safety rules in your active prompt as well.

---

## 1. Principle of Least Privilege (Read-Only by Default)

Never give your MCP server an admin-level API key unless absolutely necessary.

The safe default is:

- least-privilege access
- read-only API keys
- scope limited to only the systems and endpoints the tool actually needs

Avoid broad read-write credentials for early MCP work. If the model hallucinates, misreads intent, or loops on a bad tool call, an overly powerful key turns a harmless mistake into a real outage or data-loss event.

* **Proxmox:** Create a dedicated read-only API token so it can inspect VM states and network interfaces without delete or modify privileges.
* **Portainer/Docker:** Issue standard-user API keys that only have access to view specific environments, or use read-only Docker socket proxies if hitting the daemon directly.
* **Firewall (OPNsense/pfSense):** Restrict the API user groups to `Diagnostics` or `Status` pages. Block all `POST/PUT/DELETE` API routes for the MCP user.

If you are ever tempted to start with a read-write key "just for testing," stop and redesign the test. Early validation should happen with exported sample data or narrow read-only access.

## 2. Execution Constraints & Human-in-the-Loop

If you *must* build a tool that modifies state (e.g., spinning down a container or pushing a firewall rule), you must build a safety catch:
* **The "Dry-Run" Pattern:** The MCP tool should default to a "dry-run" behavior where it simply prints out the exact command it *intends* to run. The user must then manually review it before giving the LLM a secondary approval to execute.
* **Never Expose Raw Shells:** Do not give an LLM an open `ssh_execute` tool where it can pass any arbitrary bash command. Instead, build specific tools like `restart_container(container_id)` that handle the SSH execution safely behind the scenes.

## 3. Network Isolation

* **VLAN Segmentation:** Place your MCP server (or Jump-Host) on an isolated Management VLAN. Restrict its outbound network access so it can **only** talk to the specific APIs it needs (for example, your container API endpoint and your firewall management API endpoint).
* **Zero-Trust Tunnels:** If querying from a local laptop, use Tailscale or WireGuard ACLs to ensure the laptop can only hit the MCP server and not the broader infrastructure.

## 4. Rate Limiting & Timeouts

LLMs can sometimes get confused, hallucinate loops, or repeatedly call the same tool if they don't get the answer they expect.
* **Timeouts:** Ensure every HTTP request in your MCP server code has a strict timeout (e.g., 5 seconds) so it doesn't hang the client.
* **Rate Limits:** Implement basic memory rate-limiting in your tool logic so the LLM cannot spam your firewall API 50 times a second and accidentally DDoS your own network.

## 5. Prompt Discipline

Be specific when you prompt the model.

Good prompts for MCP work usually say:

- what system you want to inspect
- what data source to use
- whether the task is sample-data or live-data
- that the task is read-only
- what exact output you want back

Vague prompts make it easier for the model to guess, overreach, or choose the wrong tool. Specific prompts lower the chance of hallucinated actions and make review easier.

---
*Stay paranoid, stay secure, and happy automating.*
