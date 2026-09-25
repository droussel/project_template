---
description: Independently review a candidate against a real base
argument-hint: "<feature-dir> <base-ref>"
---
Read `.pi/agents/reviewer.md` and follow it with the project's authorities.
Feature directory: $1
Comparison base ref: $2

If either is missing, ask; do not invent the ref. Inspect HEAD and uncommitted
changes as well as the diff. Write review findings, not source fixes. The operator
starts a fresh Pi session when independent context is required.
