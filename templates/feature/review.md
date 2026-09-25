# Independent review: {{FEATURE_TITLE}}

## Scope and verdict

Assignment: {{REVIEW_SCOPE}}

Candidate and comparison baseline: {{COMMITS_AND_UNCOMMITTED_STATE}}

Requirements/architecture read: {{PATHS}}

Verdict: {{NO_BLOCKING_FINDINGS_OR_REPAIR_REQUIRED_OR_INCOMPLETE_EVIDENCE}}

Reviewed versus not reviewed: {{BOUNDARIES_AND_LIMITATIONS}}

No numerical quality score. Do not infer correctness from a test count alone.

## Confirmed findings

### {{SEVERITY}} — {{SPECIFIC_TITLE}}

ID: {{STABLE_LOCAL_FINDING_ID}}

- Expected behavior / authority: {{CONTRACT}}
- Actual behavior: {{OBSERVATION}}
- Evidence: {{EXACT_FILE_SYMBOL_LINES_AND_EXECUTION_PATH}}
- Reproduction: {{INPUTS_COMMANDS_STATE_AND_OBSERVED_RESULT}}
- Impact: {{REAL_USER_OR_SYSTEM_CONSEQUENCE}}
- Why existing tests miss it: {{BOUNDARY_GAP}}
- Smallest correction direction: {{INVARIANT_TO_RESTORE_NOT_A_PATCH}}

Use Critical for trust/state corruption or similarly serious impact, High for major
normal-use failure, Medium for narrower real defects, and Low for small correctness
or usability issues. Justify severity; do not report stylistic preference as a defect.

## Approved-plan gaps

{{REQUIRED_BEHAVIOR_OMITTED_OR_NONE}}

Separate gaps from bugs, deliberate deferrals, and proposals outside the assignment.

## UX / documentation findings

{{ACTUAL_OPERATOR_OR_USER_FRICTION_WITH_EVIDENCE_OR_NONE}}

## Unverified risks

{{UNCERTAIN_FINDINGS_AND_WHAT_EVIDENCE_IS_MISSING}}

An unrun integration is not automatically a confirmed defect. Do not infer success
from a mock or failure from an unsupported environment without tracing the boundary.

## Important invariants verified

{{CHECKED_BEHAVIOR_THAT_WORKS_WITH_EVIDENCE}}

## Commands and experiments

| Command / sequence | Environment and candidate | Outcome | Evidence |
|---|---|---|---|
| {{COMMAND}} | {{CONTEXT}} | {{RESULT}} | {{PATH_OR_SUMMARY}} |

## Repair order and acceptance

{{DEPENDENCY_AND_RISK_ORDER_FOR_CONFIRMED_FINDINGS}}

A targeted re-review should reproduce changed boundaries; do not silently demand an
unbounded new audit or expand the accepted scope after each repair.

## Repository state

Initial state: {{STATUS}}

Final state: {{STATUS}}

Source, configuration, and tests were not modified by review. List the authorized
report output and any temporary material; never discard pre-existing user changes.

## Finding disposition (completed by the responsible implementer/operator later)

| ID | Fixed / accepted risk / rejected / deferred | Rationale and regression/evidence |
|---|---|---|
| {{ID}} | {{STATUS}} | {{EVIDENCE}} |
