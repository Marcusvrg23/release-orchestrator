# Provider-agnostic model routing

The core skill does not name provider models because model catalogs and pricing change faster than workflow policy.

## Capability tiers

### FAST

Use for low-ambiguity, mostly deterministic work:

- file discovery;
- code/document search;
- log scanning;
- command-output classification;
- simple diff inspection;
- narrow test execution or result extraction.

### BALANCED

Use for ordinary engineering work:

- bounded root-cause investigation;
- implementation analysis;
- focused review;
- test-plan design;
- source reconciliation.

### STRONG

Use when stronger reasoning/coding materially reduces rework:

- difficult implementation;
- substantial investigation;
- cross-file synthesis;
- nontrivial migration analysis;
- coordination of an explicitly assigned independent workstream.

### FRONTIER

Reserve for high ambiguity or consequence:

- architecture decisions;
- security boundaries;
- payment/financial behavior;
- destructive migrations;
- incident hypotheses with costly failure modes;
- final adversarial review of a high-risk release.

## Selection rule

Choose the least expensive tier likely to complete the assigned role reliably. Escalate when evidence shows the current tier is insufficient; do not escalate merely for prestige.

## Reasoning effort

If the host exposes an effort control, scale it with ambiguity and consequence rather than task length alone. Deterministic retrieval may need low effort; a small but security-critical change may need high effort.

Do not rely on exact effort labels across providers. Treat provider-specific names as adapter configuration.

## Single-model hosts

If only one model is available, keep the same protocol and reduce cost by:

- narrowing scope;
- avoiding duplicate workers;
- using deterministic tools for deterministic questions;
- loading references on demand;
- preserving prior valid evidence.

## Runtime truth

A requested model or tier is not proof of runtime identity. Only claim the actual model/effort when the host exposes authoritative confirmation.

## Updating provider maps

Provider-specific examples belong in adapters or release notes, not in this core reference. This keeps the skill valid when model generations change.
