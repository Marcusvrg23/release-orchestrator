# Release Orchestrator v1.0.0

> **Ship with evidence, not agent confidence.**

Release Orchestrator is a provider-agnostic Agent Skill for release engineering, debugging, incident response, security-sensitive review, and high-risk code changes.

Its central rule is simple: **delegation must earn its cost**. The root agent stays responsible for the task, specialists are bounded and evidence-producing, and material claims are verified before a release decision.

## Highlights

- root-only execution by default;
- explicit delegation gate before spawning specialists;
- evidence-over-consensus verification;
- runtime capability discovery instead of assumed tools;
- provider-neutral model tiers: `FAST`, `BALANCED`, `STRONG`, `FRONTIER`;
- isolated writable workers only when the host actually provides isolation;
- minimal-blast-radius change policy;
- proportional validation and evidence freshness rules;
- adapters for OpenAI Codex, Claude Code, Gemini CLI, Cursor, GitHub Copilot, and generic agent harnesses;
- examples for bug fixes, incidents, release readiness, and security reviews;
- MIT licensed portable `SKILL.md` bundle.

## Core workflow

```text
UNDERSTAND -> REPRODUCE -> ISOLATE -> CHANGE -> VERIFY -> PRESERVE -> DECIDE
```

## Portable bundle

```text
skills/release-orchestrator/
```

Copy that directory into the Agent Skills discovery path supported by your host. See `adapters/` and `docs/compatibility.md` for host-specific guidance.

## Philosophy

More agents are not automatically more intelligence. Release Orchestrator favors the smallest useful coordination structure and requires evidence before confidence.
