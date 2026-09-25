# Implementation architecture: {{FEATURE_TITLE}}

Status: {{DRAFT_READY_FOR_OPERATOR_REVIEW_OR_EXPLICITLY_APPROVED}}

Inputs / inspected baseline: {{SPEC_SCOUT_COMMIT_AND_WORKTREE_CONTEXT}}

This document describes one proposed change. `ARCHITECTURE.md` at repository root
remains the current system map. Do not claim approval that the operator did not give.

## 1. Behavior, scope, and non-goals

{{ACCEPTANCE_CRITERIA_IMPORTANT_INVARIANTS_AND_BOUNDED_CHANGE}}

## 2. Current implementation and proposed direction

{{EXISTING_MECHANISMS_ACTUAL_SYMBOLS_AND_SMALLEST_COHERENT_DIRECTION}}

Distinguish inspected facts from inference. Include the relevant source references
and contradictions discovered since the Scout report, rather than trusting it blindly.

## 3. Affected layers and responsibilities

| Layer / subsystem | Current owner | Change / unchanged boundary | Relevant files |
|---|---|---|---|
| {{REAL_LAYER}} | {{OWNER}} | {{DELTA}} | {{PATHS}} |

Use actual layers, not a mandatory UI/service/repository pattern. Cover every affected
layer, including diagnostics, configuration, and user docs when the feature touches them.

## 4. Components and boundary contracts

| Existing / new symbol | Caller → receiver | Inputs and result/error | Owner / lifetime | Compatibility |
|---|---|---|---|---|
| {{REAL_OR_PROPOSED_SYMBOL}} | {{EDGE}} | {{TYPED_CONTRACT}} | {{RULE}} | {{IMPACT}} |

Specify meaningful types/functions/interfaces/events/schemas, not every helper.
Show signatures or typed payload examples when ambiguity would force the implementer
to invent architecture. Do not force object-oriented constructs onto a non-OO design.

## 5. End-to-end call and data flow

{{ENTRY_TO_BOUNDARY_TO_AUTHORITY_TO_STATE_OR_EFFECT_TO_FEEDBACK}}

For each consequential edge, identify payload, sync/async behavior, ordering,
ownership transfer, error return, and notification path. Include at least the main
success path and the most important failure path. Use a diagram only if useful.

## 6. State ownership and lifecycle

{{CREATOR_WRITER_READER_AUTHORITY_DERIVED_STATE_INVALIDATION_AND_CLEANUP}}

Name the exact publication/commit boundary when stale data can race. Separate
persisted facts from process-local memory; account for restart if it matters.

## 7. Failure, recovery, and execution semantics

{{VALIDATION_PARTIAL_EFFECTS_RETRY_OWNER_CANCELLATION_TIMEOUT_AND_RECOVERY}}

{{THREAD_PROCESS_TASK_OWNERSHIP_ORDERING_REENTRANCY_SHUTDOWN_AND_BOUNDS}}

Do not add transactions/queues/retries where unnecessary. Where needed, define the
failure behavior precisely enough to implement and test across the real boundary.

## 8. Persistence, compatibility, and external constraints

{{FORMAT_SCHEMA_MIGRATION_DEFAULTS_ROLLOUT_ROLLBACK_TRUST_AND_EXTERNAL_API_IMPACT}}

Include secrets/untrusted input, performance/resource constraints, and observability
only where material. Do not invent unsupported numeric targets or new infrastructure.

## 9. UX and user-documentation impact

{{USER_TASK_STATES_ACCESSIBILITY_ERROR_GUIDANCE_DOC_PAGES_AND_EXAMPLES}}

Link existing `DESIGN.md` and design-system rules rather than duplicating them.
For no user-visible change, state that briefly with the reason.

## 10. Verification and acceptance evidence

| Criterion / invariant ID | Symbol / flow / boundary | Test/check and location | Fixture/environment | Manual evidence if needed |
|---|---|---|---|---|
| AC1 | {{BOUNDARY}} | {{REAL_OR_PLANNED_TEST}} | {{CONTEXT}} | {{CHECK_OR_NONE}} |

Name actual `scripts/check` / `scripts/verify` phases and native commands when known.
Distinguish existing checks from proposed ones. Include negative/stale/restart paths
where the design depends on them. Coverage and file size do not replace behavior proof.

Required completion gate for this feature: {{FINITE_AGREED_GATE}}

Evidence not available to an automated agent: {{EXPLICIT_MANUAL_OR_EXTERNAL_LIMIT}}

## 11. Simplicity and blast radius

- Existing mechanisms extended: {{MECHANISMS}}
- New concepts/components: {{ONLY_JUSTIFIED_ADDITIONS_OR_NONE}}
- Each new abstraction: {{PURPOSE_COMPLEXITY_HIDDEN_AND_WHY_EXISTING_IS_INSUFFICIENT}}
- Material alternatives rejected: {{DECISIVE_TRADEOFFS_NOT_AN_EXHAUSTIVE_CATALOGUE}}
- Adjacent work deliberately excluded: {{OUT_OF_SCOPE}}
- Why this is the smallest complete design: {{RATIONALE}}

Do not assign a simplicity score. Do not require a refactor merely to make the plan
look architectural. Decompose files by cohesion while respecting project size limits.

## 12. Delivery sequence

| Slice | Coherent change and owned paths | Verification / handoff |
|---|---|---|
| 1 | {{COMPLETE_TESTABLE_SLICE}} | {{GATE}} |

Set dependencies and exclusive write ownership. A multi-file change does not require
multiple implementers. Do not automatically spawn agents or schedule paid execution.

## 13. Applicability and readiness

Review every lens. Expand affected ones above; group concise N/A reasons here instead
of manufacturing pages of boilerplate.

| Lens | Covered above, or not affected because... |
|---|---|
| Behavior / scope | {{ANSWER}} |
| Existing mechanisms | {{ANSWER}} |
| All affected layers | {{ANSWER}} |
| Important contracts | {{ANSWER}} |
| End-to-end flow | {{ANSWER}} |
| State / lifetime | {{ANSWER}} |
| Failure / recovery | {{ANSWER}} |
| Concurrency / execution | {{ANSWER}} |
| Persistence / compatibility | {{ANSWER}} |
| Trust / integrations / resources / observability | {{ANSWER}} |
| UX / user documentation | {{ANSWER}} |
| Verification | {{ANSWER}} |
| Simplicity / delivery | {{ANSWER}} |

Unresolved material decisions: {{QUESTIONS_OR_NONE}}

Do not call this implementation-ready with unchosen material alternatives or TBDs
in behavior, boundaries, ownership, concurrency, persistence, security, or acceptance.
Private helpers and reversible local algorithms may remain with the implementer.
