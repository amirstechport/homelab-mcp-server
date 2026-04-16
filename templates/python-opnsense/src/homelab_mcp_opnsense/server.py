"""Read-only OPNsense-oriented MCP starter using the official Python SDK."""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any

from mcp.server.fastmcp import FastMCP


SERVER_NAME = os.getenv("OPNSENSE_STARTER_NAME", "OPNsense Starter")
RULES_FILE = Path(os.getenv("OPNSENSE_RULES_FILE", "./sample_data/firewall_rules.json"))
ALIASES_FILE = Path(os.getenv("OPNSENSE_ALIASES_FILE", "./sample_data/firewall_aliases.json"))
DOCS_ROOT = Path(os.getenv("OPNSENSE_DOCS_ROOT", "./output"))

mcp = FastMCP(SERVER_NAME)


def _read_json(path: Path) -> Any:
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


@mcp.tool()
def opnsense_server_info() -> dict[str, Any]:
    """Return starter metadata for smoke testing."""
    return {
        "server_name": SERVER_NAME,
        "rules_file": str(RULES_FILE),
        "rules_file_exists": RULES_FILE.exists(),
        "aliases_file": str(ALIASES_FILE),
        "aliases_file_exists": ALIASES_FILE.exists(),
        "docs_root": str(DOCS_ROOT),
        "mode": "read-only sample-data starter",
    }


@mcp.tool()
def opnsense_rule_summary() -> dict[str, Any]:
    """Summarize exported firewall rules."""
    rules = _read_json(RULES_FILE)
    enabled = [rule for rule in rules if rule.get("enabled", True)]
    by_interface: dict[str, int] = {}
    for rule in enabled:
        iface = rule.get("interface", "unknown")
        by_interface[iface] = by_interface.get(iface, 0) + 1
    return {
        "total_rules": len(rules),
        "enabled_rules": len(enabled),
        "rules_by_interface": by_interface,
        "sample_rules": enabled[:10],
    }


@mcp.tool()
def opnsense_alias_summary() -> dict[str, Any]:
    """Summarize exported firewall aliases."""
    aliases = _read_json(ALIASES_FILE)
    summarized = []
    for alias in aliases[:20]:
        summarized.append(
            {
                "name": alias.get("name", ""),
                "type": alias.get("type", ""),
                "entry_count": len(alias.get("entries", [])),
                "description": alias.get("description", ""),
            }
        )
    return {
        "alias_count": len(aliases),
        "aliases": summarized,
    }


@mcp.tool()
def render_firewall_markdown(title: str = "Firewall Summary") -> str:
    """Render a small markdown summary from exported rules and aliases."""
    rules = _read_json(RULES_FILE)
    aliases = _read_json(ALIASES_FILE)
    lines = [
        f"# {title}",
        "",
        f"- rule count: `{len(rules)}`",
        f"- alias count: `{len(aliases)}`",
        "",
        "## Sample Rules",
        "",
    ]
    for rule in rules[:5]:
        lines.append(
            f"- `{rule.get('interface', 'unknown')}` | `{rule.get('action', 'pass')}` | "
            f"`{rule.get('source', 'any')}` -> `{rule.get('destination', 'any')}`"
        )
    lines.append("")
    lines.append("## Sample Aliases")
    lines.append("")
    for alias in aliases[:5]:
        lines.append(
            f"- `{alias.get('name', '')}` ({alias.get('type', '')}) - "
            f"{len(alias.get('entries', []))} entries"
        )
    return "\n".join(lines)


def main() -> None:
    mcp.run()


if __name__ == "__main__":
    main()
