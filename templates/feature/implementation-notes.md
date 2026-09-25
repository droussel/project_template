# Implementation notes: {{FEATURE_TITLE}}

## Assignment and baseline

Approved inputs: {{SPEC_ARCHITECTURE_AND_OPERATOR_INSTRUCTION}}

Starting revision / worktree: {{COMMIT_AND_PREEXISTING_CHANGES}}

Owned paths / excluded paths: {{SCOPE}}

## Implemented behavior

{{OBSERVABLE_CHANGES_AND_IMPORTANT_SYMBOLS}}

## Deviations and decisions

{{DIFFERENCES_FROM_PLAN_WITH_REASONS_AND_APPROVAL_WHERE_REQUIRED}}

Do not silently replace architectural decisions. Update the plan only to reflect
explicit decisions and actual progress, not to make an incomplete implementation look done.

## Verification

| Command or manual check | Candidate / environment | Result | Evidence location / limitation |
|---|---|---|---|
| `scripts/check` | {{CONTEXT}} | {{PASS_FAIL_NOT_RUN}} | {{EVIDENCE}} |
| `scripts/verify` | {{CONTEXT}} | {{PASS_FAIL_NOT_RUN}} | {{EVIDENCE}} |

Regression added for each fixed defect: {{PATH_AND_BEHAVIOR}}

Coverage groups and size warnings affected: {{RESULTS_NOT_JUST_AGGREGATE}}

Use exact results; distinguish unavailable tooling from failing product behavior.
Do not claim a provider, OS, browser, device, restart, or interaction was exercised
unless it actually was.

## User and durable documentation

{{UPDATED_GUIDES_REFERENCE_EXAMPLES_ARCHITECTURE_DESIGN_OR_NO_IMPACT_REASON}}

## Review and remaining work

Self-review: {{WHAT_WAS_INSPECTED}}

Independent review: {{REPORT_OR_PENDING_OR_NOT_REQUIRED_REASON}}

Unresolved findings / manual checks: {{ITEMS_OR_NONE}}

## Handoff

Current revision / dirty status: {{ACTUAL_STATUS}}

Next required operator action: {{REVIEW_ACCEPT_OR_NARROW_REPAIR}}

Do not automatically commission another agent or move into a new milestone.
