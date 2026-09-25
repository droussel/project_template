# {{FEATURE_TITLE}}

Status: {{DRAFT_OR_APPROVED_AND_ACTUAL_APPROVAL_EVIDENCE}}

## Goal and user outcome

{{WHAT_CHANGES_FOR_WHOM_AND_WHY}}

## Scope and non-goals

- In scope: {{BEHAVIOR_THIS_CHANGE_OWNS}}
- Out of scope: {{ADJACENT_WORK_WE_ARE_NOT_DOING}}
- Constraints: {{COMPATIBILITY_RESOURCES_PLATFORM_AND_DEPENDENCY_LIMITS}}

## Current and desired behavior

Current observed behavior: {{REPOSITORY_OR_USER_EVIDENCE}}

Desired behavior: {{CONCRETE_OBSERVABLE_OUTCOME}}

## Main workflow and meaningful states

{{USER_ACTION_TO_RESULT_AND_IMPORTANT_FAILURE_OR_RECOVERY_PATH}}

For user-facing work, link `DESIGN.md` and consider initial/empty, working, success,
invalid input, cancellation, and failure only where relevant. For CLI/library work,
cover caller ergonomics and errors instead of inventing screens.

## Acceptance criteria

| ID | Observable requirement | How it can be demonstrated |
|---|---|---|
| AC1 | {{REQUIREMENT}} | {{TEST_OR_EXPLICIT_MANUAL_EVIDENCE}} |

Use stable IDs. Criteria should describe behavior and important invariants, not
implementation guesses or a particular test-framework call.

## Important decisions

{{DECISION_AND_REASON_OR_LINK_TO_AN_ACCEPTED_RECORD}}

## Risks and open questions

{{MATERIAL_UNRESOLVED_QUESTIONS_AND_SPECIFIC_OWNER_OR_NEXT_ACTION}}

Do not mark the specification approved or settled while material product intent is
unresolved. Reversible implementation details may remain with the implementer.

## Documentation impact

{{QUICK_START_GUIDE_REFERENCE_EXAMPLES_TROUBLESHOOTING_OR_NO_USER_IMPACT}}

## Handoff

Repository / base revision: {{EXACT_CONTEXT}}

Related authorities/artifacts: {{PATHS}}

Next explicitly requested activity: {{SCOUT_ARCHITECTURE_IMPLEMENTATION_OR_OTHER}}
