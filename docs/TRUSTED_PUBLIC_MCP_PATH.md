# 🧱 Trusted Public MCP Path

Use this path if you want to start with well-known public MCP building blocks before building a custom homelab server.

## When This Path Makes Sense

Choose this path if:

- you want a simpler first step
- you are not ready to design your own MCP server yet
- you want to learn MCP using public reference servers and official SDKs first

## Good Starting Points

- The official MCP organization and SDKs: [modelcontextprotocol on GitHub](https://github.com/modelcontextprotocol)
- The MCP reference servers maintained by the MCP steering group: [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)
- Official client documentation for the tool you plan to use:
  - Claude Code overview: https://docs.anthropic.com/en/docs/claude-code/overview
  - OpenAI Codex overview: https://help.openai.com/en/articles/11369540

## Recommended Beginner Path

1. Start with an official MCP SDK or reference server.
2. Connect it to one MCP-capable client.
3. Learn the basic server/client flow with public-safe tooling first.
4. Only then decide whether you really need a custom homelab server.

## Important Note

The MCP reference servers are useful starting points, but they are reference implementations, not a guarantee that every server is production-ready for your environment. Read the project docs carefully and keep your first integrations read-only.

## When To Come Back To This Repo

Come back to the custom server path when:

- you need homelab-specific outputs
- you want topology or markdown generation around your own environment
- you need custom firewall, virtualization, proxy, or observability workflows
- you are ready to own the safety model yourself
