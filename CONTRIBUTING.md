# Contributing

Thank you for improving Release Orchestrator.

## Principles for contributions

Changes should preserve the project's core properties:

- provider-agnostic core;
- root ownership of material decisions;
- bounded delegation;
- evidence-first validation;
- explicit consequential-action boundaries;
- minimal context and permission footprint.

Provider-specific behavior belongs in adapters unless it is part of the open Agent Skills contract.

## Pull requests

A useful pull request should explain:

```text
PROBLEM
WHY THE CORE OR ADAPTER SHOULD CHANGE
BEHAVIOR BEFORE
BEHAVIOR AFTER
COMPATIBILITY IMPACT
VALIDATION
```

Avoid adding current provider model slugs to the portable core. Avoid pre-authorizing broad shell/tool access.

Security-sensitive reports should follow `SECURITY.md` rather than a public issue when disclosure could create unnecessary risk.
