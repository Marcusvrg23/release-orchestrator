# Release Orchestrator — Launch Kit

> **Ship with evidence, not agent confidence.**

Canonical repository: https://github.com/Marcusvrg23/release-orchestrator

## Positioning

Release Orchestrator is an Agent Skill for AI coding agents that decides **when not to delegate**, bounds specialist work, protects existing behavior, and requires evidence before release-sensitive claims.

Primary line:

> **The orchestration protocol that decides when NOT to use another agent.**

Secondary line:

> **More agents are not automatically more intelligence. Delegation must earn its cost.**

## Fast demo commands

```bash
gh skill preview Marcusvrg23/release-orchestrator release-orchestrator
gh skill install Marcusvrg23/release-orchestrator release-orchestrator
```

## Show HN draft

**Title:** Show HN: Release Orchestrator – an Agent Skill that decides when not to spawn another agent

Multi-agent coding has a coordination problem: more agents can mean duplicated investigation, conflicting edits, context bloat, and false confidence.
I built Release Orchestrator around the opposite default: root-only execution unless delegation earns its cost.

It gives coding agents a provider-agnostic protocol for:
- deciding whether a specialist is actually useful;
- keeping workers read-only unless isolation is real;
- minimizing blast radius;
- validating material claims against authoritative evidence;
- preserving evidence freshness across a release;
- keeping consequential actions behind explicit authorization.

The core is a portable `SKILL.md` bundle and works without subagents too.

Preview:
`gh skill preview Marcusvrg23/release-orchestrator release-orchestrator`

Install:
`gh skill install Marcusvrg23/release-orchestrator release-orchestrator`

Repo: https://github.com/Marcusvrg23/release-orchestrator

I would especially value feedback on the delegation gate and evidence model.

## Reddit draft

**Title:** I open-sourced an Agent Skill that defaults to *not* spawning subagents

A lot of agent workflows optimize for fan-out. I wanted the opposite default.

Release Orchestrator starts at zero workers and only delegates when a bounded specialist can produce distinct evidence or materially reduce uncertainty.

Its core loop is:

```text
UNDERSTAND -> REPRODUCE -> ISOLATE -> CHANGE -> VERIFY -> PRESERVE -> DECIDE
```
It is provider-agnostic and uses capability tiers instead of hard-coding model names, so the core does not become stale every time model catalogs change.

It also treats worker output as evidence, not authority: a subagent saying "fixed" is never enough by itself.

Preview:
`gh skill preview Marcusvrg23/release-orchestrator release-orchestrator`

GitHub:
https://github.com/Marcusvrg23/release-orchestrator

Feedback welcome, especially from people using Codex, Claude Code, Gemini CLI, Cursor, Copilot, or custom agent harnesses.

## LinkedIn draft

I just open-sourced **Release Orchestrator v1.0.0**.

The idea came from a problem I kept seeing in AI-assisted software work: adding more agents does not automatically create better engineering.

Sometimes it creates duplicated investigation, conflicting edits, larger context, and confidence without proof.

So Release Orchestrator uses a different rule:

**Delegation must earn its cost.**

It is a provider-agnostic Agent Skill that helps coding agents decide when to stay root-only, when a bounded specialist is worth using, how to minimize blast radius, and what evidence is required before calling work fixed or release-ready.

**Ship with evidence, not agent confidence.**

Preview it with:
`gh skill preview Marcusvrg23/release-orchestrator release-orchestrator`

Repository:
https://github.com/Marcusvrg23/release-orchestrator
## X / Threads draft

Open-sourced Release Orchestrator v1.0.0.

An Agent Skill built around one rule:

**Delegation must earn its cost.**

Root-only by default.
Bounded specialists when useful.
Evidence over agent confidence.
Minimal blast radius.

`gh skill preview Marcusvrg23/release-orchestrator release-orchestrator`

https://github.com/Marcusvrg23/release-orchestrator

## Short video script — 45 seconds

**0–6s**  
Text: "More agents != more intelligence"  
Voice: "Multi-agent coding can create more coordination cost than value."

**6–14s**  
Show: one root agent, then five unnecessary workers.  
Text: "Duplicate investigation. Conflicting edits. Context bloat."

**14–24s**  
Show Release Orchestrator delegation gate.  
Voice: "Release Orchestrator starts with zero workers and asks whether delegation will produce distinct evidence."

**24–34s**  
Show: ROOT -> SPECIALIST -> EVIDENCE -> ROOT VERIFICATION.  
Voice: "Workers stay bounded. Their output is evidence, not authority."

**34–41s**  
Show core workflow.  
Text: "UNDERSTAND -> REPRODUCE -> ISOLATE -> CHANGE -> VERIFY -> PRESERVE -> DECIDE"

**41–45s**  
Text: "Ship with evidence, not agent confidence."  
Show repo name and `gh skill preview` command.
## Suggested publishing order

1. GitHub repository and release are the canonical source.
2. Show HN with the technical thesis, not marketing language.
3. One targeted Reddit post per relevant community; adapt the intro instead of cross-posting identical copy.
4. LinkedIn with the engineering lesson and project link.
5. X / Threads with the one-line thesis and preview command.
6. A short demo video or GIF in follow-up posts.
7. Submit to relevant Agent Skills / Copilot community collections where contribution rules permit.

## Response template for technical feedback

Thanks for checking it out. The core is intentionally provider-agnostic: it discovers runtime capabilities and only delegates when the delegation gate passes. If you hit a host-specific mismatch, please include the host, installation path, available capabilities, and the smallest reproducible task.

## What not to claim

Do not claim that Release Orchestrator:
- guarantees correctness;
- makes every task faster;
- always reduces token usage;
- supports a host capability the runtime has not proven;
- replaces CI, security scanners, deployment platforms, or human release authority.
