# Architecture

<!-- TEMPLATE: describe the real, current system. Remove inapplicable sections.
This is not the architect's task prompt or a per-feature implementation plan.
Do not keep illustrative layers as if they existed. -->

## Scope and non-goals

- System/repository responsibility: {{CURRENT_SCOPE}}
- External actors and systems: {{ACTUAL_ACTORS_AND_INTEGRATIONS}}
- Explicit exclusions: {{NON_GOALS}}
- Current implementation status: {{WHAT_EXISTS_VERSUS_WHAT_IS_ONLY_PROPOSED}}

## Architectural goals and invariants

{{SMALL_SET_OF_DURABLE_REQUIREMENTS}}

Use observable constraints: ownership, determinism, safety, data integrity,
compatibility, isolation, portability, resource behavior, or testability. Do not
invent numerical targets or require layers that the system does not need.

## System shape

{{ACTUAL_COMPONENTS_AND_PRIMARY_END_TO_END_FLOW}}

Add a diagram only when it clarifies actual boundaries. Identify authoritative
components and distinguish adapters, projections, and caches.

## Dependency direction

Allowed dependencies: {{ACTUAL_ALLOWED_DIRECTIONS}}

Forbidden dependencies: {{IMPORTANT_FORBIDDEN_EDGES}}

Mechanical enforcement, when practical: {{REAL_CHECK_OR_NOT_YET_IMPLEMENTED}}

## Major subsystem responsibilities

### {{SUBSYSTEM_NAME}}

- Owns: {{BEHAVIOR_AND_STATE}}
- Does not own: {{BOUNDARIES}}
- Depends on / used by: {{ACTUAL_CONTRACTS_AND_CONSUMERS}}
- Important interfaces: {{STABLE_BOUNDARIES_WITH_SOURCE_REFERENCES}}
- Failure/lifecycle constraints: {{MATERIAL_RULES}}

Repeat only for architecturally significant subsystems, not every helper or file.
Link detailed subsystem contracts when this root map is no longer sufficient.

## State, authority, and lifetime

| State or data | Authoritative owner / mutation path | Derived copies | Lifetime / invalidation |
|---|---|---|---|
| {{STATE}} | {{OWNER}} | {{CACHE_OR_VIEW_OR_NONE}} | {{RULE}} |

Define synchronization when state crosses threads/processes. Do not introduce a
second writable source of truth merely for presentation or telemetry.

## Execution and important flows

{{SIGNIFICANT_SYNC_ASYNC_PROCESS_THREAD_AND_OWNERSHIP_FLOW}}

Cover error return, partial effects, cancellation, retry ownership, ordering, and
shutdown where those change correctness. Link a detailed flow rather than copying
an exhaustive implementation call graph into this map.

## External, persistence, and trust boundaries

{{APIS_STORAGE_PLATFORM_VENDOR_AND_UNTRUSTED_INPUT_BOUNDARIES}}

Where relevant, name formats, schema compatibility, migration/crash-safety rules,
secrets handling, isolation, and which component validates each boundary.
Do not document capabilities the implementation does not provide.

## Hard quality boundaries

{{PROPERTIES_THAT_MUST_REMAIN_TRUE_DURING_FAILURE_OR_OVERLOAD}}

Project-wide size, coverage, formatting, and linting policies live in
`CONTRIBUTING.md`, not here. This section contains system-specific invariants.

## Verification architecture

| Material risk / invariant | Boundary being exercised | Deterministic or manual evidence |
|---|---|---|
| {{RISK}} | {{BOUNDARY}} | {{ACTUAL_TEST_COMMAND_FIXTURE_OR_MANUAL_CHECK}} |

Name real checks and distinguish existing from planned evidence. Do not equate
coverage or mocked success with cross-process/integration correctness.

## Accepted decisions, exceptions, and questions

- Accepted rationale: {{LINKS_TO_MATERIAL_DECISIONS_WHEN_THEY_EXIST}}
- Known exception: {{REASON_RISK_AND_REMOVAL_CONDITION_OR_NONE}}
- Unresolved material question: {{QUESTION_OR_NONE}}

Update this map when accepted implementation changes responsibilities, dependencies,
state authority, important contracts, or hard constraints. Historical reasoning belongs
in decision records; feature-specific proposals belong with the feature.
