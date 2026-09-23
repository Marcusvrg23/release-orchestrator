# Release Orchestrator v1.0.1

> **Ship with evidence, not agent confidence.**

Release Orchestrator is a provider-agnostic Agent Skill for release engineering, debugging, incident response, security-sensitive review, and high-risk code changes.

Its central rule is simple: **delegation must earn its cost**. The root agent stays responsible for the task, specialists are bounded and evidence-producing, and material claims are verified before a release decision.

## What's new in v1.0.1

- official GitHub CLI Agent Skills quick start:
  - `gh skill preview Marcusvrg23/release-orchestrator release-orchestrator`
  - `gh skill install Marcusvrg23/release-orchestrator release-orchestrator`
- animated delegation/evidence demo in the README;
- social-preview asset and reproducible launch-asset generator;
- launch kit for Show HN, Reddit, LinkedIn, X / Threads, and short video;
- clearer differentiation from deployment/versioning tools with the same generic name;
- GitHub secret scanning and push protection enabled;
- rulesets protecting `main` history and immutable `v*` release tags.

## Core workflow

```text
UNDERSTAND -> REPRODUCE -> ISOLATE -> CHANGE -> VERIFY -> PRESERVE -> DECIDE
```
## Core guarantees of the protocol

- root-only execution by default;
- explicit delegation gate before spawning specialists;
- evidence-over-consensus verification;
- runtime capability discovery instead of assumed tools;
- provider-neutral model tiers: `FAST`, `BALANCED`, `STRONG`, `FRONTIER`;
- isolated writable workers only when the host actually provides isolation;
- minimal-blast-radius change policy;
- proportional validation and evidence freshness rules;
- adapters for OpenAI Codex, Claude Code, Gemini CLI, Cursor, GitHub Copilot, and generic agent harnesses;
- MIT licensed portable `SKILL.md` bundle.

## Portable bundle

```text
skills/release-orchestrator/
```

Preview before installing:

```bash
gh skill preview Marcusvrg23/release-orchestrator release-orchestrator
```

## Philosophy

More agents are not automatically more intelligence. Release Orchestrator favors the smallest useful coordination structure and requires evidence before confidence.
