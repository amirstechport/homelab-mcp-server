# 💬 Starter Prompts

These prompts are for the "lazy but cautious" path: let your LLM scaffold the first version of your MCP server, but keep the scope small enough that you can still review it safely.

Use them with caution:

- start with sample data
- keep the server read-only
- review what the model generates before running it
- do not treat generated code as trusted until you inspect it

If you plan to use repo-level instruction files such as `CLAUDE.md` or `AGENTS.md`, do not assume the client is honoring them yet. Until you verify that behavior in your chosen client, put the important safety rules directly in the prompt too.

## Best First Use

If you want the fastest useful onboarding flow:

1. Use one of the prompts below to scaffold a tiny starter.
2. Run it locally with sample data only.
3. Attach it to one MCP-capable client.
4. Verify it with [Interact With Your MCP Server](./INTERACT_WITH_MCP.md).

That is enough for a first win.

## Fastest Cautious Prompt

Use this if you want your LLM to help you scaffold a starter without designing everything manually:

```text
Help me build a minimal read-only MCP server for local testing.

Constraints:
- Python only
- sample data first
- no live infrastructure yet
- no write actions
- keep the server small and easy to understand
- include one basic info tool, one inventory summary tool, and one proxy summary tool
- include a short README with run steps

I want the smallest possible working MCP server that I can connect to an MCP-capable client and test safely.
```

## Repo-Aware Shortcut Prompt

Use this if you want your LLM to lean on this repo instead of inventing a structure from scratch:

```text
Use this repo as a reference and help me get to a first MCP win quickly.

Plan:
- start from the smallest safe path
- keep the server read-only
- use sample data only
- keep the implementation easy to review

Deliver:
- one minimal MCP server
- one README with exact run steps
- one sample MCP client config example
- one smoke test prompt I can use to confirm the server is active

Do not add:
- write actions
- SSH execution
- live credentials
- broad infrastructure access
```

## Better Prompt For This Repo

Use this if you want the model to work from this repo structure:

```text
Use the python-minimal starter in this repo as the base.

Task:
- explain how it works
- keep everything read-only
- help me customize it for my environment using exported sample data first
- do not add live API calls yet
- do not add state-changing tools

My goal is one quick win: run the server, connect it to my client, and successfully call one sample tool.
```

## Prompt For A Firewall-First Path

```text
Help me build a read-only firewall-focused MCP server using exported sample data first.

Requirements:
- summarize firewall rules
- summarize aliases
- render markdown output
- no live credentials yet
- no write actions
- include a clear README and one smoke test
```

## Prompt For A VM/Container Path

```text
Help me build a read-only MCP server for virtualization and container inventory.

Requirements:
- use exported guest and container data
- summarize hosts and services
- render simple markdown output
- no live credentials yet
- no restart, redeploy, or delete actions
```

## Prompt For The Lazy But Cautious Path

This is the "let the LLM do more of the scaffolding" version, but keep it constrained:

```text
I want the fastest path to a safe MCP proof of concept.

Build me a small read-only MCP server with:
- sample data
- one starter README
- one config example for an MCP client
- one basic health/info tool
- one sample summary tool

Rules:
- no live API keys
- no SSH execution
- no write actions
- keep the code simple enough for me to review
- explain how I verify that the MCP server is active in my client
```

## Prompt For Verification

After the server is built, use this:

```text
Help me verify that this MCP server is actually working.

I want to confirm:
- the client sees the server
- the tools are available
- one read-only tool call succeeds

Do not jump to advanced use cases yet. Keep this to a safe smoke test only.
```

## Red Flags

Do not accept a generated starter blindly if it:

- adds write actions by default
- asks for live credentials before sample-data testing
- exposes raw shell execution
- skips the README or test steps
- makes the code much larger than it needs to be
