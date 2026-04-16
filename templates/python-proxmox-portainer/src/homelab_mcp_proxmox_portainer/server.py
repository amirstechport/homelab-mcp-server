"""Read-only Proxmox and Portainer oriented MCP starter."""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any

from mcp.server.fastmcp import FastMCP


SERVER_NAME = os.getenv("PLATFORM_STARTER_NAME", "Proxmox Portainer Starter")
PROXMOX_GUESTS_FILE = Path(
    os.getenv("PROXMOX_GUESTS_FILE", "./sample_data/proxmox_guests.json")
)
PORTAINER_CONTAINERS_FILE = Path(
    os.getenv("PORTAINER_CONTAINERS_FILE", "./sample_data/portainer_containers.json")
)
DOCS_ROOT = Path(os.getenv("PLATFORM_DOCS_ROOT", "./output"))

mcp = FastMCP(SERVER_NAME)


def _read_json(path: Path) -> Any:
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


@mcp.tool()
def platform_server_info() -> dict[str, Any]:
    """Return starter metadata for smoke testing."""
    return {
        "server_name": SERVER_NAME,
        "proxmox_guests_file": str(PROXMOX_GUESTS_FILE),
        "proxmox_guests_exists": PROXMOX_GUESTS_FILE.exists(),
        "portainer_containers_file": str(PORTAINER_CONTAINERS_FILE),
        "portainer_containers_exists": PORTAINER_CONTAINERS_FILE.exists(),
        "docs_root": str(DOCS_ROOT),
        "mode": "read-only sample-data starter",
    }


@mcp.tool()
def proxmox_guest_summary() -> dict[str, Any]:
    """Summarize exported Proxmox guests."""
    guests = _read_json(PROXMOX_GUESTS_FILE)
    running = [guest for guest in guests if guest.get("status") == "running"]
    by_type: dict[str, int] = {}
    for guest in guests:
        gtype = guest.get("type", "unknown")
        by_type[gtype] = by_type.get(gtype, 0) + 1
    return {
        "guest_count": len(guests),
        "running_count": len(running),
        "guests_by_type": by_type,
        "guests": guests[:15],
    }


@mcp.tool()
def portainer_container_summary() -> dict[str, Any]:
    """Summarize exported Portainer containers."""
    containers = _read_json(PORTAINER_CONTAINERS_FILE)
    running = [c for c in containers if c.get("state") == "running"]
    by_host: dict[str, int] = {}
    for container in containers:
        host = container.get("host", "unknown")
        by_host[host] = by_host.get(host, 0) + 1
    return {
        "container_count": len(containers),
        "running_count": len(running),
        "containers_by_host": by_host,
        "containers": containers[:20],
    }


@mcp.tool()
def render_platform_markdown(title: str = "Platform Inventory Summary") -> str:
    """Render a small markdown summary from Proxmox and Portainer exports."""
    guests = _read_json(PROXMOX_GUESTS_FILE)
    containers = _read_json(PORTAINER_CONTAINERS_FILE)
    lines = [
        f"# {title}",
        "",
        f"- Proxmox guests: `{len(guests)}`",
        f"- Portainer containers: `{len(containers)}`",
        "",
        "## Sample Guests",
        "",
    ]
    for guest in guests[:5]:
        lines.append(
            f"- `{guest.get('name', '')}` | `{guest.get('type', '')}` | "
            f"`{guest.get('status', '')}` | `{guest.get('node', '')}`"
        )
    lines.append("")
    lines.append("## Sample Containers")
    lines.append("")
    for container in containers[:5]:
        lines.append(
            f"- `{container.get('name', '')}` | `{container.get('image', '')}` | "
            f"`{container.get('host', '')}` | `{container.get('state', '')}`"
        )
    return "\n".join(lines)


def main() -> None:
    mcp.run()


if __name__ == "__main__":
    main()
