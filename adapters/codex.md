# OpenAI Codex adapter

## Install

For project-scoped skills, place the canonical bundle at:

```text
.agents/skills/release-orchestrator/
```

For a user-scoped installation, use the current Codex-supported user skills directory or the supported skill installer for your Codex version.

Do not use `.codex/skills/` unless current Codex documentation for your version explicitly says it is a discovery root.

## Subagents

Release Orchestrator does not bundle mandatory Codex custom agents. If you want stable specialist personas, Codex custom agents are a separate mechanism from Skills and should be configured according to current Codex subagent documentation.

The skill remains functional without custom agents.

## Model routing

Map `FAST`, `BALANCED`, `STRONG`, and `FRONTIER` to models available in the active Codex runtime. Do not hard-code model slugs into the portable skill.

Current OpenAI model guidance explicitly supports tuning how much a capable model delegates to subagents and recommends calibrating testing to the change. Release Orchestrator intentionally keeps delegation conservative by default and broadens testing only when risk or new evidence justifies it.

## Permissions

Do not use this skill to bypass Codex sandbox, approval, or production permissions. Consequential actions remain separate user-authorized operations.
