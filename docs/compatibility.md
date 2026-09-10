# Compatibility matrix

This document records the host behavior that Release Orchestrator was designed against for the `v1.0.0` candidate.

Last reviewed: **2026-09-10**.

The canonical portable bundle is:

```text
skills/release-orchestrator/
```

The core never assumes that a host exposes shell access, Git, subagents, model selection, or isolated writable workers. Those capabilities are discovered at runtime.

| Host | Native `SKILL.md` support | Project location(s) | Notes |
|---|---|---|---|
| OpenAI Codex | Yes | `.agents/skills/<name>/` in supported project workflows | Custom subagents are a separate Codex mechanism; keep model/effort configuration outside the portable core. |
| Claude Code | Yes | `.claude/skills/<name>/` | Personal skills can live under `~/.claude/skills/`. Claude also supports uploaded custom Skills in other products/API surfaces. |
| Gemini CLI | Yes | `.agents/skills/<name>/` or `.gemini/skills/<name>/` | The cross-agent `.agents/skills/` path takes precedence over `.gemini/skills/` at the same scope when both contain the same skill. Use `/skills list` to verify discovery and `/skills reload` after changes. |
| Cursor | Yes | `.agents/skills/<name>/` or `.cursor/skills/<name>/` | Cursor also loads compatible Claude/Codex skill directories and supports GitHub-imported skills. |
| GitHub Copilot | Yes | `.agents/skills/<name>/`, `.github/skills/<name>/`, or `.claude/skills/<name>/` on supported surfaces | Keep broad shell permissions outside the portable skill and review host permissions separately. |
| Generic LLM / custom harness | Prompt-mode fallback | host-defined | Supply the core instructions through the harness and enable only capabilities that really exist. |

## OpenAI-specific evolution incorporated into V1

The private precursor used a fixed model-routing policy and a conservative two-specialist ceiling. Current Codex releases support richer subagent workflows, including custom agent definitions and configurable defaults for subagent model/reasoning/concurrency.

Release Orchestrator incorporates those changes without becoming Codex-specific:

- concurrency now starts at 0 and normally caps at 2, but can exceed 2 when genuinely independent work and host isolation justify it;
- model selection is expressed as `FAST`, `BALANCED`, `STRONG`, and `FRONTIER` capability tiers;
- requested model/effort is never treated as proof of actual runtime identity;
- isolated writing workers are allowed only when the host provides real isolation and the user has authorized implementation;
- custom provider agents remain adapter configuration rather than portable core policy.

## Security portability

The canonical `SKILL.md` intentionally leaves host tool authorization outside the portable bundle. Hosts differ in permission semantics, so Release Orchestrator preserves the user's runtime permission model instead of assuming broad execution rights.

## Versioning rule

Provider model names, paths, and CLI commands may change independently of the orchestration protocol. Update adapters and this compatibility matrix when a host changes; change the core only when the provider-neutral behavior itself needs to evolve.
