# Cursor adapter

Cursor supports Agent Skills using the open `SKILL.md` format. Install the canonical bundle in the skill directory supported by your Cursor version.

Keep provider-specific rules, modes, hooks, and model preferences outside the portable `SKILL.md` so the same bundle remains usable in other hosts.

## Delegation

Only set `SPAWN_AGENTS=true` when the active Cursor runtime exposes a real subagent or parallel-agent mechanism. Only set `ISOLATE_WORKERS=true` when those workers have separate writable state.

Without those capabilities, Release Orchestrator runs root-only.
