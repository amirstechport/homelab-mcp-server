"""Minimal homelab-oriented MCP starter using the official Python SDK.

Primary sources used for this starter:
- Official MCP Python SDK README quickstart and direct execution examples
- Official MCP SDK docs index
"""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any

from mcp.server.fastmcp import FastMCP


SERVER_NAME = os.getenv("STARTER_SERVER_NAME", "Homelab Starter")
INVENTORY_FILE = Path(os.getenv("STARTER_INVENTORY_FILE", "./sample_data/inventory.ini"))
PROXY_ROUTES_FILE = Path(
    os.getenv("STARTER_PROXY_ROUTES_FILE", "./sample_data/proxy_routes.json")
)
DOCS_ROOT = Path(os.getenv("STARTER_DOCS_ROOT", "./output"))

mcp = FastMCP(SERVER_NAME)


def _read_text_file(path: Path) -> str:
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")
    return path.read_text(encoding="utf-8")


def _parse_inventory(text: str) -> list[dict[str, str]]:
    hosts: list[dict[str, str]] = []
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line or line.startswith("[") or line.startswith("#") or line.startswith(";"):
            continue
        parts = line.split()
        hostname = parts[0]
        ip = ""
        group = ""
        for part in parts[1:]:
            if part.startswith("ansible_host="):
                ip = part.split("=", 1)[1]
            if part.startswith("group="):
                group = part.split("=", 1)[1]
        hosts.append({"hostname": hostname, "ip": ip, "group": group})
    return hosts


@mcp.tool()
def starter_server_info() -> dict[str, Any]:
    """Return basic server metadata for smoke testing."""
    return {
        "server_name": SERVER_NAME,
        "inventory_file": str(INVENTORY_FILE),
        "inventory_exists": INVENTORY_FILE.exists(),
        "proxy_routes_file": str(PROXY_ROUTES_FILE),
        "proxy_routes_exists": PROXY_ROUTES_FILE.exists(),
        "docs_root": str(DOCS_ROOT),
    }


@mcp.tool()
def inventory_summary() -> dict[str, Any]:
    """Read a local inventory export and summarize discovered hosts."""
    text = _read_text_file(INVENTORY_FILE)
    hosts = _parse_inventory(text)
    groups = sorted({host["group"] for host in hosts if host["group"]})
    return {
        "host_count": len(hosts),
        "groups": groups,
        "hosts": hosts[:20],
    }


@mcp.tool()
def proxy_route_summary() -> dict[str, Any]:
    """Read a local JSON export of proxy routes and summarize backends."""
    raw = _read_text_file(PROXY_ROUTES_FILE)
    data = json.loads(raw)
    routes = data if isinstance(data, list) else data.get("routes", [])
    summarized = []
    for route in routes[:20]:
        summarized.append(
            {
                "name": route.get("name", ""),
                "domain": route.get("domain", ""),
                "target": route.get("target", ""),
                "type": route.get("type", ""),
            }
        )
    return {
        "route_count": len(routes),
        "routes": summarized,
    }


@mcp.tool()
def render_host_markdown(hostname: str, ip: str, role: str, notes: str = "") -> str:
    """Render a small markdown block for a host record."""
    lines = [
        f"### `{hostname}`",
        "",
        f"- IP: `{ip}`",
        f"- role: {role}",
    ]
    if notes:
        lines.append(f"- notes: {notes}")
    return "\n".join(lines)


def main() -> None:
    """Entry point for direct execution."""
    mcp.run()


if __name__ == "__main__":
    main()
