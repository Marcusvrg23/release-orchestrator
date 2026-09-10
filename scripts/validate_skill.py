#!/usr/bin/env python3
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "release-orchestrator" / "SKILL.md"

text = SKILL.read_text(encoding="utf-8")
errors = []

if not text.startswith("---\n"):
    errors.append("SKILL.md must begin with YAML frontmatter")

parts = text.split("---", 2)
if len(parts) < 3:
    errors.append("SKILL.md frontmatter is not closed")
    frontmatter = ""
else:
    frontmatter = parts[1]

name_match = re.search(r"^name:\s*(.+)$", frontmatter, re.MULTILINE)
desc_match = re.search(r"^description:\s*(.+)$", frontmatter, re.MULTILINE)

if not name_match:
    errors.append("missing name")
else:
    name = name_match.group(1).strip()
    if not re.fullmatch(r"[a-z0-9-]{1,64}", name):
        errors.append(f"invalid skill name characters/length: {name!r}")
    if name.startswith("-") or name.endswith("-") or "--" in name:
        errors.append(f"invalid skill name hyphen placement: {name!r}")
    if name != SKILL.parent.name:
        errors.append(
            f"skill name must match parent directory: name={name!r}, directory={SKILL.parent.name!r}"
        )

if not desc_match:
    errors.append("missing description")
else:
    description = desc_match.group(1).strip()
    if not description:
        errors.append("description must not be empty")
    if len(description) > 1024:
        errors.append("description exceeds 1024 characters")
    if "<" in description or ">" in description:
        errors.append("description must not contain XML-like tags")

if len(text.splitlines()) > 500:
    errors.append("SKILL.md exceeds the recommended 500-line limit")

for forbidden in ["orchestrate-diego", "Plataforma de Concursos", "Diego Lima"]:
    if forbidden.lower() in text.lower():
        errors.append(f"private precursor marker found in public SKILL.md: {forbidden}")

if "allowed-tools:" in frontmatter:
    errors.append("portable core must not pre-authorize tools")

if errors:
    for error in errors:
        print(f"ERROR: {error}")
    sys.exit(1)

print("release-orchestrator SKILL.md validation passed")
