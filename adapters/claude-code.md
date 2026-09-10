# Claude Code adapter

Use Claude Code's current Agent Skills installation convention and copy the canonical `skills/release-orchestrator/` bundle into the supported project or personal skills directory for your version.

If `.claude/skills/<skill-name>/SKILL.md` is supported in your installed version, the resulting path is typically:

```text
.claude/skills/release-orchestrator/SKILL.md
```

Keep the portable `SKILL.md` unchanged. Put Claude-specific model aliases, hooks, agents, or permission configuration outside the portable core.

## Delegation

If Claude Code exposes subagents, use the same delegation gate. The availability of subagents is not itself a reason to use them.

Writing workers require actual isolation and disjoint ownership. Otherwise keep specialists read-only.

## Effort/model selection

Provider model names and thinking controls evolve. Map them to the capability tiers at runtime rather than embedding versioned model names in the skill.
