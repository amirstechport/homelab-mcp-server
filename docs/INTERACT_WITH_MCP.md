# Interact With Your MCP Server

This page is about the moment after setup: how to talk to your MCP server, how to know it is active in your client, and how to get a clean first success.

## The Basic Idea

Your MCP server is only useful when your LLM client can actually see it and call its tools.

That means your first goal is not "use every feature." Your first goal is:

- the server is configured
- the client sees it
- the tools are visible
- one safe read-only tool call works

## Greenlight Checklist

Use this checklist before trusting the setup:

1. The MCP server is configured in your client.
2. The client has been restarted or reloaded after configuration.
3. The server shows up in the client as connected or available.
4. The tools are visible.
5. One harmless read-only tool call succeeds.
6. If you are relying on `CLAUDE.md`, `AGENTS.md`, or similar instruction files, you have verified that this client/session actually honors them.

If any one of those fails, treat the MCP server as not ready yet.

## What To Ask First

Start with small, safe prompts:

- `List the tools available from this MCP server.`
- `Call the basic server info tool and show me the result.`
- `Read the sample inventory and summarize the hosts.`
- `Summarize the sample proxy routes.`

Do not start with:

- live firewall changes
- SSH execution
- bulk infrastructure audits
- write actions

## Client Notes

The exact interaction style depends on the LLM client you choose.

### Claude Code

Claude Code has documented MCP management commands and a built-in MCP view.

Useful checks:

- `claude mcp list`
- `claude mcp get <server-name>`
- `/mcp`

What to look for:

- your configured server is listed
- Claude Code shows connection status
- available tools and prompts are visible

Once that looks good, ask Claude Code to call one read-only tool.

### Claude Desktop

Claude Desktop is usually the simplest local MCP test surface.

Greenlight steps:

1. Add the MCP server to the Claude Desktop config.
2. Fully restart Claude Desktop.
3. Ask for one small tool-backed action, such as:
   - `Show me the tools from the connected MCP server.`
   - `Call the server info tool.`

If Claude cannot see tools or never offers tool use, the MCP server is not active yet.

### Codex

How MCP appears depends on whether you are using the Codex CLI, IDE extension, or app surface.

Use a practical check:

1. Start the Codex surface you plan to use.
2. Confirm the MCP server or plugin/integration is configured there.
3. Ask for a tiny read-only tool action:
   - `List the tools available from the connected MCP server.`
   - `Run the basic server info tool.`

If the client cannot enumerate or use the tools, treat the server as not active yet.

### Google Antigravity

The exact MCP workflow depends on the agent/editor setup you attach there.

Use the same practical check:

1. Confirm the MCP integration is configured in the workspace.
2. Reload the workspace or restart the app if needed.
3. Ask for one safe read-only tool action:
   - `List the tools available from the MCP server.`
   - `Call the server info tool.`

If no tools appear, the MCP server is not greenlit yet.

## First Real Success

Your first successful interaction should be something like:

- tool list works
- server info works
- sample inventory summary works

That is enough to prove the path works.

Only after that should you move on to:

- more advanced starters
- live APIs
- custom outputs
- deployment on a jump host
