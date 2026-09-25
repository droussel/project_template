---
description: Review one material risk in a candidate
argument-hint: "<feature-dir> <base-ref> <focus>"
---
Read `.pi/agents/specialist-reviewer.md` and follow it with the project's relevant
authorities and feature inputs.
Feature directory: $1
Comparison base ref: $2
Material risk to examine: ${@:3}

If any input is missing, ask before reviewing. Do not silently expand the focus,
spawn another reviewer or modify source.
