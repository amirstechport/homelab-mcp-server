# 🚀 Quick Start

This is the fastest path to a first MCP win in this repo.

## Who This Is For

Use this path if you want:

- one working MCP server quickly
- no live infrastructure yet
- a safe read-only-first starting point

## Fastest Path

1. Go to [Choose a Starter](../templates/README.md).
2. Start with [python-minimal](../templates/python-minimal/README.md).
3. Copy `.env.example` to `.env`.
4. Run the starter with sample data.
5. Attach it to one MCP client.
6. Call one read-only tool successfully.

If you only want one clean first success, stop there. You do not need live APIs yet.

## What Success Looks Like

Your first quick win is simple:

- the starter runs
- your MCP client sees the tools
- one sample read-only tool call works

Do not start with live firewall or hypervisor APIs if all you need is proof that the flow works.

## Lazy But Cautious Shortcut

If you want the quickest possible path, you can let your LLM scaffold the first version of the server for you.

Keep that shortcut safe:

- use [Starter Prompts](./STARTER_PROMPTS.md)
- keep the first version read-only
- use sample data first
- review the generated code before you run it
- confirm the server is really active with [Interact With Your MCP Server](./INTERACT_WITH_MCP.md)

## After That

- If you want your LLM to scaffold the starter for you, read [Starter Prompts](./STARTER_PROMPTS.md).
- If you want to verify the client/server connection, read [Interact With Your MCP Server](./INTERACT_WITH_MCP.md).
- If you want a custom server path, read [Advanced Custom Server Path](./ADVANCED_CUSTOM_SERVER_PATH.md).
- If you do not want to build your own server yet, read [Trusted Public MCP Path](./TRUSTED_PUBLIC_MCP_PATH.md).
- Before connecting live systems, read [SECURITY.md](../SECURITY.md).
