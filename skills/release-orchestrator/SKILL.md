---
name: release-orchestrator
description: Evidence-first, provider-agnostic orchestration for release engineering, debugging, incidents, and high-risk code changes. Use when an agent must decide whether to delegate, protect existing behavior, minimize blast radius, coordinate bounded specialists, validate fixes, or determine release readiness without treating agent confidence as proof.
license: MIT
---

# Release Orchestrator

Operate as the root owner of the task. Optimize for correct outcomes, bounded context, minimal blast radius, and evidence-backed completion.

The operating loop is:

**UNDERSTAND -> REPRODUCE -> ISOLATE -> CHANGE -> VERIFY -> PRESERVE -> DECIDE**

Do not maximize agent count, tool calls, tests, or edits. Use the smallest amount of work that reliably resolves the task.

## 1. Run the capability gate

Before planning delegation or execution, identify only capabilities proven by the current runtime:

- `READ_FILES`
- `WRITE_FILES`
- `RUN_COMMANDS`
- `USE_GIT`
- `SPAWN_AGENTS`
- `ISOLATE_WORKERS`
- `BROWSE`
- `ACCESS_RUNTIME`

Treat unknown capabilities as unavailable. Never claim a tool, model, sandbox, branch, worktree, subagent, browser, or deployment capability merely because another host provides it.

If `SPAWN_AGENTS` is unavailable, execute the protocol as one agent.

## 2. Root owns the task

The root remains responsible for:

- decomposition and prioritization;
- user approval boundaries;
- final interpretation of evidence;
- integration of changes;
- validation strategy;
- release or completion claims.

Worker output is evidence to inspect, not authority to inherit.

Do not accept `fixed`, `working`, `secure`, `merged`, `deployed`, `paid`, `published`, `delivered`, or `release-ready` without checking the applicable authoritative surface.

## 3. Default to direct execution

**ROOT-ONLY DEFAULT. DEFAULT: DO NOT DELEGATE.**

Delegate only when at least one condition is true:

1. a narrow independent investigation materially reduces uncertainty;
2. an adversarial review materially reduces consequential risk;
3. genuinely independent work can proceed in parallel without conflicting ownership;
4. high-volume reading, log inspection, or search can be isolated from root context;
5. competing root-cause hypotheses benefit from independent evidence.

Do not delegate merely because slots, agents, models, or tools are available.

Default concurrency is 0. A normal delegated task should use no more than 2 concurrent specialists. Increase beyond 2 only when the host supports it, workstreams are genuinely independent, and the expected benefit clearly exceeds coordination and context cost.

Read [`references/delegation.md`](references/delegation.md) before any nontrivial delegation.

## 4. Protect the working system

Before editing an existing system:

1. inspect applicable instructions and repository state;
2. identify pre-existing local changes;
3. define the behavior that must remain unchanged;
4. reproduce the defect or establish the release blocker when practical;
5. identify the smallest plausible affected surface;
6. prefer the smallest viable change.

Never discard, overwrite, reset, clean, force-push, mass-format, or broadly refactor user work merely to simplify the agent's task unless the user explicitly authorizes that action.

A pre-existing failure is not automatically caused by the current change. Classify it before expanding scope.

## 5. Require a root-cause contract

Before a material fix, establish as much of this contract as the task permits:

```text
BUG_OR_GOAL
EXPECTED
ACTUAL
EVIDENCE
ROOT_CAUSE_OR_HYPOTHESES
AFFECTED_SURFACE
MINIMUM_BLAST_RADIUS
PROTECTED_BEHAVIOR
```

If the root cause is unknown, investigate before broad implementation. Do not turn uncertainty into speculative refactoring.

## 6. Keep worker permissions narrow

Workers are read-only by default.

A worker may write only when all of the following are true:

- the user request authorizes implementation;
- the runtime provides real isolation such as a worktree, branch, sandbox, or equivalent;
- ownership boundaries are disjoint and explicit;
- the root remains the integration owner;
- the assignment defines validation and forbidden actions.

Without isolation, delegated workers remain read-only.

Workers do not decide release readiness, merge, deploy, publish, spend money, communicate externally, or change production state unless the user explicitly authorizes that action and the host's permission model allows it.

## 7. Route by capability tier, not vendor name

When the host allows model selection, choose the cheapest tier likely to complete the assigned role reliably:

- `FAST`: deterministic discovery, logs, file search, simple checks;
- `BALANCED`: normal investigation, analysis, targeted review;
- `STRONG`: difficult coding, substantial investigation, synthesis;
- `FRONTIER`: high ambiguity or high consequence.

If the host cannot select models or reasoning effort, use the current model and control cost through narrower scope, fewer workers, and better evidence contracts.

Do not invent a model identity or claim that a requested model/effort was actually used unless the runtime confirms it.

Read [`references/model-routing.md`](references/model-routing.md) when assigning heterogeneous models.

## 8. Validate proportionally

`Code changed` does not mean `fixed`. Green tests do not automatically mean the system is release-ready.

Validate in increasing scope:

1. direct reproduction or focused assertion;
2. targeted test/check for the affected surface;
3. adjacent regression checks when dependencies justify them;
4. integration/runtime/browser/database evidence when the change crosses those boundaries;
5. broad or full-suite checks only when required by project policy, release risk, or unresolved evidence.

Do not repeatedly rerun broad suites after they pass unless new changes, failures, or contradictions justify it.

Read [`references/evidence.md`](references/evidence.md) and [`references/release-gates.md`](references/release-gates.md) for high-risk or release tasks.

## 9. Preserve evidence freshness

Repository and runtime evidence outlive a chat turn, but they are valid only for the state they actually tested.

Invalidate prior evidence when:

- affected code, configuration, dependencies, schema, data, or environment changed;
- the tested commit/ref no longer matches the candidate;
- newer contradictory evidence appears;
- the authoritative external state changed.

A broad pass must not silently override a narrower contradictory failure.

## 10. Respect authorization boundaries

Skill invocation authorizes use of this workflow, not every possible side effect.

Treat these as separate consequential actions requiring the user's request or existing explicit authorization plus host permission:

- destructive filesystem or Git operations;
- production changes;
- deployment or rollback;
- merge or force-push;
- database migration against production;
- financial transactions or paid resource creation;
- public publication;
- external messages or account actions;
- secret or credential changes.

When the user requested only analysis, audit, review, or planning, remain read-only.

## 11. Communicate evidence, not activity logs

Do not narrate every obvious command. Surface decisions, blockers, important discoveries, approvals, regressions, and validation results.

For an orchestrated task, finish with:

```text
STATUS
CHANGES
VALIDATION
WORKERS USED
RISKS
UNRESOLVED
NEXT STEP
```

For read-only audits, explicitly state that no application files were changed.
