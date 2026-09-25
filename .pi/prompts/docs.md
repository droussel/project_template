---
description: Update and validate user documentation
argument-hint: "<feature-dir> <documentation-task>"
---
Read `.pi/agents/technical-writer.md` and follow it with project authorities.
Feature directory (or `none` for standalone documentation): $1
Documentation task: ${@:2}

If the task is missing or ambiguous, ask for it. Inspect actual behavior rather
than documenting only a plan. Do not publish a site without authorization.
