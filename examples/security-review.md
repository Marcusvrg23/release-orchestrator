# Example: security-sensitive change

User request:

```text
Review this authentication change before release.
```

Recommended behavior:

- stay read-only unless implementation is requested;
- map authentication/authorization trust boundaries;
- identify affected entry points and protected behavior;
- inspect tests and runtime assumptions;
- consider one independent adversarial reviewer because consequence is high;
- validate concrete attack surfaces rather than producing a generic checklist;
- separate proven vulnerabilities, plausible risks, and unknowns;
- require stronger evidence before declaring the change secure or release-ready.
