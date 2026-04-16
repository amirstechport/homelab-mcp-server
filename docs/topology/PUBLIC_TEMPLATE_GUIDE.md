# Public Topology Template Guide

This is the public-safe topology entry point for the repo.

## Primary Public Artifact

- [HomeLab_OPNsense_PUBLIC_TEMPLATE.png](./HomeLab_OPNsense_PUBLIC_TEMPLATE.png)

## What This File Is

This PNG is the sanitized public topology artifact derived from the private working topology. It preserves the general structure, layout style, and MCP-driven documentation story without exposing private hostnames, domains, or internal IP space.

The topology graphic itself was assembled in Excalidraw, then exported as a public-safe PNG for the repo.

## What Was Sanitized

- hostnames were replaced with generic labels
- internal IP addresses were removed from visible labels
- private domains and public-facing service names were removed from visible labels
- node roles were rewritten as reusable examples

## How To Reuse It

1. Use the PNG as the public reference artifact.
2. Replace the generic host labels with your own hostnames in your own working copy.
3. Add your own IPs, domains, and service names where appropriate.
4. Remove any lanes that do not apply to your environment.
5. Export your own PNG or SVG for sharing.

## Suggested Replacement Pattern

- `Firewall / OPNsense` -> your firewall hardware and platform
- `Hypervisor B / Secondary Proxmox` -> your virtualization node
- `Docker Host A / core services` -> your main container host
- `Jump Host / management` -> your automation or bastion host
- `AI Host` -> your ML or document workload host
- `Blog VM` -> any dedicated app VM
- `NAS / storage + backups` -> your storage target

## Related Files

- [PUBLIC_TOPOLOGY_SUMMARY.md](./PUBLIC_TOPOLOGY_SUMMARY.md)
