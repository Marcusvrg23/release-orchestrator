# Evidence protocol

Evidence is the basis for high-confidence claims.

## Evidence hierarchy

Prefer the most authoritative surface available for the claim:

1. production or target runtime state, when safely readable and relevant;
2. deterministic tests or commands against the actual candidate state;
3. repository code/configuration and commit/ref state;
4. application/browser/database integration evidence;
5. logs and telemetry with known provenance;
6. worker analysis;
7. model opinion.

The hierarchy is contextual. A unit test cannot prove a production environment variable exists; a screenshot cannot prove a database migration is correct.

## Evidence record

For material findings, capture enough context to make the claim reproducible:

```text
CLAIM
SOURCE
STATE_OR_REF
COMMAND_OR_OBSERVATION
RESULT
SCOPE
FRESHNESS
CONTRADICTIONS
```

## Contradictory evidence

When evidence conflicts:

- do not average the conclusions;
- prefer the more authoritative and more specific evidence;
- verify whether the evidence tested different states;
- reproduce the narrower failure when practical;
- keep the gate open until the contradiction is resolved.

A broad green suite does not erase a reproducible narrow failure.

## Freshness

Evidence is stale when the state it validated changed materially. Common invalidators:

- new commit affecting the same path or dependency;
- environment/configuration change;
- schema or migration change;
- data mutation relevant to the assertion;
- deployment change;
- dependency lockfile update;
- external API/provider state change.

Do not rerun unaffected evidence merely because a new chat/session started.

## Claims requiring stronger proof

Use stronger evidence for:

- security and authorization boundaries;
- payments and financial calculations;
- authentication and account access;
- destructive data operations;
- migrations;
- deployment and rollback;
- public release readiness.

## Negative evidence

Absence of an observed failure is weaker than positive confirmation of expected behavior. Prefer assertions that prove the desired invariant directly.
