"""Read-only observability-focused MCP starter."""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any

from mcp.server.fastmcp import FastMCP


SERVER_NAME = os.getenv("OBS_STARTER_NAME", "Observability Starter")
METRICS_FILE = Path(os.getenv("OBS_METRICS_FILE", "./sample_data/metrics_snapshot.json"))
LOGS_FILE = Path(os.getenv("OBS_LOGS_FILE", "./sample_data/log_events.json"))
MONITORS_FILE = Path(os.getenv("OBS_MONITORS_FILE", "./sample_data/monitors.json"))
DOCS_ROOT = Path(os.getenv("OBS_DOCS_ROOT", "./output"))

mcp = FastMCP(SERVER_NAME)


def _read_json(path: Path) -> Any:
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


@mcp.tool()
def observability_server_info() -> dict[str, Any]:
    """Return starter metadata for smoke testing."""
    return {
        "server_name": SERVER_NAME,
        "metrics_file": str(METRICS_FILE),
        "metrics_exists": METRICS_FILE.exists(),
        "logs_file": str(LOGS_FILE),
        "logs_exists": LOGS_FILE.exists(),
        "monitors_file": str(MONITORS_FILE),
        "monitors_exists": MONITORS_FILE.exists(),
        "docs_root": str(DOCS_ROOT),
        "mode": "read-only sample-data starter",
    }


@mcp.tool()
def metrics_summary() -> dict[str, Any]:
    """Summarize exported metrics snapshot data."""
    metrics = _read_json(METRICS_FILE)
    return {
        "metric_count": len(metrics),
        "metrics": metrics[:20],
    }


@mcp.tool()
def log_summary() -> dict[str, Any]:
    """Summarize exported log events."""
    events = _read_json(LOGS_FILE)
    by_level: dict[str, int] = {}
    for event in events:
        level = event.get("level", "unknown")
        by_level[level] = by_level.get(level, 0) + 1
    return {
        "event_count": len(events),
        "events_by_level": by_level,
        "events": events[:20],
    }


@mcp.tool()
def monitor_summary() -> dict[str, Any]:
    """Summarize exported service monitor states."""
    monitors = _read_json(MONITORS_FILE)
    by_status: dict[str, int] = {}
    for monitor in monitors:
        status = monitor.get("status", "unknown")
        by_status[status] = by_status.get(status, 0) + 1
    return {
        "monitor_count": len(monitors),
        "monitors_by_status": by_status,
        "monitors": monitors[:20],
    }


@mcp.tool()
def render_observability_markdown(title: str = "Observability Summary") -> str:
    """Render a small markdown summary from observability sample data."""
    metrics = _read_json(METRICS_FILE)
    events = _read_json(LOGS_FILE)
    monitors = _read_json(MONITORS_FILE)
    lines = [
        f"# {title}",
        "",
        f"- metrics tracked: `{len(metrics)}`",
        f"- log events: `{len(events)}`",
        f"- monitors: `{len(monitors)}`",
        "",
        "## Monitor Sample",
        "",
    ]
    for monitor in monitors[:5]:
        lines.append(
            f"- `{monitor.get('name', '')}` | `{monitor.get('status', '')}` | "
            f"`{monitor.get('target', '')}`"
        )
    lines.append("")
    lines.append("## Recent Log Sample")
    lines.append("")
    for event in events[:5]:
        lines.append(
            f"- `{event.get('level', '')}` | `{event.get('service', '')}` | "
            f"{event.get('message', '')}"
        )
    return "\n".join(lines)


def main() -> None:
    mcp.run()


if __name__ == "__main__":
    main()
