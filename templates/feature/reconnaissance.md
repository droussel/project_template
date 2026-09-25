# Repository reconnaissance: {{FEATURE_TITLE}}

## Scope and evidence baseline

Feature spec: {{PATH}}

Repository, commit, branch, and worktree changes: {{ACTUAL_BASELINE}}

Inspected areas: {{FILES_AND_BOUNDARIES_ACTUALLY_READ}}

Not inspected / unavailable: {{LIMITATIONS}}

## Relevant implementation map

| File / module | Symbols or contracts | Responsibility / authority | Relevance |
|---|---|---|---|
| {{PATH}} | {{ACTUAL_SYMBOL}} | {{OWNS}} | {{WHY_IT_MATTERS}} |

Distinguish source inspection from guesses. Avoid exhaustive unrelated inventories.

## Current end-to-end flow

{{ENTRY_POINT_TO_STATE_OWNER_TO_EFFECT_TO_RESULT}}

Include important adapters, payloads, error paths, and state handoffs. Identify
uncertain dynamic edges rather than inventing a complete call graph.

## Existing mechanisms to reuse

{{COHESIVE_EXISTING_MECHANISMS_AND_WHAT_THEY_ALREADY_PROVIDE}}

This is factual reconnaissance, not the final solution design.

## State, lifecycle, and high-risk boundaries

{{AUTHORITY_DERIVED_STATE_CONCURRENCY_PERSISTENCE_TRUST_AND_RECOVERY_AS_RELEVANT}}

## Applicable authorities

{{ARCHITECTURE_DESIGN_CONTRIBUTING_DECISIONS_SUBSYSTEM_PATHS_AND_KEY_CONSTRAINTS}}

## Verification already available

| Risk / behavior | Existing test or script | What it actually proves | Known gap |
|---|---|---|---|
| {{RISK}} | {{PATH_OR_COMMAND}} | {{EVIDENCE}} | {{GAP}} |

Commands executed: {{EXACT_COMMAND_RESULTS_OR_NOT_RUN}}

## Questions for the architect

{{MATERIAL_UNKNOWN_FACTS_OR_CONFLICTS_WITH_SOURCE_REFERENCES}}

## Handoff

Priority reads: {{SMALL_SET_OF_PATHS}}

Useful raw evidence: {{PATHS_AND_RETENTION_LIMITATION}}

Next step: produce the proposed architecture; no implementation has been performed.
