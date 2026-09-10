# Example: release readiness

User request:

```text
Tell me whether this branch is ready to release.
```

Recommended behavior:

- remain read-only unless fixes are explicitly requested;
- identify the exact candidate branch/ref;
- reuse still-valid prior evidence;
- inspect known release blockers and required checks;
- run targeted or required final checks;
- use at most two bounded read-only specialists when independent evidence will help;
- resolve contradictory evidence rather than voting on it;
- report `RELEASE_READY`, `READY_FOR_FINAL_CHECK`, `NOT_READY`, or `CANNOT_RELEASE` with supporting evidence.

Do not merge, deploy, migrate production, or publish merely because the branch is judged ready.
