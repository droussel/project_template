---
description: Specify desired behavior and acceptance criteria
argument-hint: "<feature-dir> <request>"
---
Read `.pi/agents/designer.md` and follow that role with project authorities.
Feature directory: $1
Request: ${@:2}

If either input is absent, ask for it before writing. Work in the current Pi
session. Do not implement the feature or declare the spec approved for the operator.
