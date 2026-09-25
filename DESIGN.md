# Product and Interaction Design

<!-- TEMPLATE: useful without a formal design system. Keep only applicable guidance.
For a CLI/library, users include developers. Delete this document only when there
is no meaningful user/developer-facing interaction to guide. -->

## Users and jobs

- Primary users: {{WHO_USES_THIS}}
- Main task: {{THE_OUTCOME_THE_USER_IS_TRYING_TO_REACH}}
- Context: {{PLATFORM_EXPERIENCE_CONSTRAINTS_AND_ENVIRONMENT}}
- First successful use: {{OBSERVABLE_FIRST_SUCCESS}}

## Baseline design guidance

Optimize the user's task, not the internal implementation structure. Keep common
actions discoverable and low-friction. Prefer predictable behavior and platform
conventions over novelty without a demonstrated benefit.

Make current state, progress, consequences, and the next useful action understandable.
Show secondary detail on demand without hiding necessary decisions or failure evidence.
Do not fill scarce screen space with internal IDs or repeated orchestration metadata.
Keep exact technical details available for diagnosis when they matter.

Preserve user work through recoverable errors. Separate draft/proposed state from
applied state when that distinction is consequential. Do not silently interpret an
ambiguous command as a destructive action. Confirmation should explain the real
consequence, not become a ritual that teaches users to click through.

Design keyboard operation, accessible names/roles, focus behavior, legible hierarchy,
and non-color-only state communication alongside the main interaction. Apply touch,
screen reader, reduced-motion, and platform requirements where relevant.

## Primary workflows

### {{WORKFLOW_NAME}}

- Entry point and user intent: {{ENTRY}}
- Minimum steps and feedback: {{FLOW}}
- Completion and user-visible outcome: {{DONE}}
- Failure/recovery and preserved work: {{RECOVERY}}

Document only workflows whose interaction model needs to remain coherent. Link
feature proposals separately; do not present them as implemented UX.

## Information hierarchy and language

- Always visible: {{MINIMUM_CONTEXT_AND_PRIMARY_ACTION}}
- Available on demand: {{DETAILS_AND_DIAGNOSTICS}}
- Vocabulary: {{USER_LANGUAGE_AND_TERMS_TO_AVOID}}
- Navigation / focus / editing conventions: {{ESTABLISHED_RULES}}

Errors explain what happened, the effect on user work, and an actionable next step.
Keep technical evidence accessible without making a stack trace the entire experience.
Avoid repetitive success notifications when the state change is already obvious.

## States to consider

For each affected workflow, consider initial/empty, working, success, partial success,
invalid input, recoverable failure, blocking failure, and unavailable/offline states.
Consider cancellation, interrupted work, stale results, and resizing where relevant.
These are design questions, not a requirement to invent all states for every product.

## CLI / API ergonomics when applicable

Use consistent names and arguments, discoverable help, useful errors, and intentional
exit codes. Separate human and machine-readable output where needed. Make normal
operations scriptable without prompts; keep destructive intent explicit.

For APIs/libraries, make defaults and ownership clear, errors useful, and common
correct use easier than accidental misuse. Do not leak transport/implementation
concepts into user vocabulary without a reason.

## Visual conventions and optional design system

{{EXISTING_VISUAL_OR_PLATFORM_CONVENTIONS_OR_NONE_ESTABLISHED_YET}}

A formal design system is not a prerequisite. Use existing platform/components
consistently. Only extract tokens/components when repeated real needs justify them.
If an authoritative design system exists, link it here rather than duplicating it.
An optional starter lives at `templates/product/DESIGN_SYSTEM.md`.

## User documentation experience

A user's first success should be supported by a tested quick start. Task guides,
reference, and troubleshooting must match visible terminology and actual behavior.
The documentation site should be navigable, readable, accessible, and usable on
small screens. A decorative landing page is not a substitute for usable instructions.

## Non-goals

{{INTERACTION_DIRECTIONS_WE_INTENTIONALLY_DO_NOT_OPTIMIZE_FOR}}

## Validation

For a meaningful UX change, inspect the rendered result and exercise the intended
workflow, keyboard/focus behavior, relevant states, and recovery. Capture screenshots
or transcripts as supporting evidence, not a replacement for interaction checks.
Record environment, steps, expected/observed result, and untested limitations.

For a material new visual direction, settle the operator's preference using a small
number of lightweight alternatives before building an elaborate system. Do not
request approval for every spacing change or invent performance/accessibility claims.

## Established decisions

{{LINKS_TO_APPROVED_PRODUCT_DECISIONS_WHEN_NEEDED}}
