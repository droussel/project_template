---
description: Adapt this template kit to the current project
argument-hint: "<project-description>"
---
Read `.pi/agents/bootstrap.md` and the root README, then apply the complete
bootstrap assignment to the current project. Operator description: $ARGUMENTS

If no project description was given, ask one question to establish its broad
purpose. Inspect before editing. Use the role's setup checklist internally; ask
only one genuinely blocking **setup** question per message and wait for the answer.
Apply safe defaults; do not turn bootstrap into product design or implementation.
Rewrite every authority and .pi/README.md for this project, omit kit-only material,
and require `python3 scripts/check-adoption.py` to pass in the target. Once the
foundation is reported, stop. This prompt runs in the current Pi session;
it is not an installer, a fresh session or a subagent.
