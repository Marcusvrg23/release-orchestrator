# Gemini CLI / Google adapter

Gemini CLI supports Agent Skills defined by a directory containing `SKILL.md` plus optional scripts and references.

For a project skill, Gemini CLI currently discovers both:

```text
.gemini/skills/release-orchestrator/
.agents/skills/release-orchestrator/
```

The `.agents/skills/` form is a cross-agent compatibility alias and takes precedence over `.gemini/skills/` when the same skill exists in both locations at the same scope. Use only one copy in a project unless you have a specific reason to maintain both.

For user scope, Gemini CLI currently discovers:

```text
~/.gemini/skills/release-orchestrator/
~/.agents/skills/release-orchestrator/
```

Use `/skills list` to confirm discovery and `/skills reload` after adding or changing a skill during an active session.

## Capabilities

Run the capability gate from the core skill. Some Google hosts support tools or agent execution that others do not. Do not infer shell, Git, subagent, browser, or sandbox access from the Gemini model name alone.

## Model routing

Map capability tiers to the models actually offered by the active Google runtime. Keep provider model names out of the portable bundle.
