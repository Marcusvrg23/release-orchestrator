# GitHub Copilot adapter

GitHub Copilot supports Agent Skills as folders containing `SKILL.md` plus optional resources.

Project skills can be placed in supported locations including:

```text
.agents/skills/release-orchestrator/
.github/skills/release-orchestrator/
.claude/skills/release-orchestrator/
```

Personal skills can use the current Copilot-supported personal skill directories.

GitHub CLI can also install and update compatible skills from repositories. Follow the current `gh skill` documentation for the exact command available in your CLI version.

## Tool permissions

Release Orchestrator deliberately does not set `allowed-tools: shell` or `allowed-tools: bash` in the portable frontmatter. Pre-approving shell execution can remove confirmation gates, so users should review the skill and choose host permissions themselves.

## Subagents

Copilot may provide subagent behavior in some surfaces. Apply the capability and delegation gates rather than assuming availability across every Copilot product.
