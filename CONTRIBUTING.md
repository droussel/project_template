# Contributing

<!-- TEMPLATE: the engineering defaults below are intended policy. Fill the
stack-specific command/coverage map during adoption. Do not report unwired gates
as enforced. Change these defaults only through an explicit operator decision. -->

## Engineering principles

Preserve documented behavior, explicit ownership, recoverable user failures, and a
codebase that remains practical to understand and change.

Apply architectural principles through concrete outcomes, not ceremony: cohesive
responsibilities, narrow contracts, substitutable adapters, explicit domain values,
and clear dependency direction. Do not add indirection for an acronym.

Extend cohesive mechanisms before building parallel ones. A new abstraction must
hide meaningful complexity or enforce a current requirement; a one-line pass-through
layer or speculative plugin system is not automatically an improvement.

Prefer typed domain values and structured errors. Make invalid states unrepresentable
where practical. Separate authoritative state from derived data. Keep I/O, clocks,
network, OS, storage, and external integrations at deliberate testable boundaries.

User input, external-service failures, and third-party data must have explicit failure
behavior. Do not swallow errors, infer success, or retry indefinitely. Document
ordering, idempotency, cancellation, and resource bounds when correctness depends on them.

A dependency needs a demonstrated purpose, an owning layer, and an assessment of
build, platform, maintenance, security, and runtime impact. Do not add dependencies
for tasks already served clearly by the standard library or existing project tooling.
Unsafe or privileged operations require the narrowest possible boundary and an
explanation of why their outward contract is safe.

## Stack and command map

| Concern | Actual project choice / command |
|---|---|
| Languages and toolchain versions | {{PINNED_OR_SUPPORTED_TOOLCHAINS}} |
| Dependency setup | {{REPRODUCIBLE_SETUP_COMMAND}} |
| Formatter, check-only mode | {{FORMAT_CHECK_COMMAND}} |
| Linter / static analysis | {{LINT_COMMAND_AND_RULESET}} |
| Type checking, when separate | {{TYPECHECK_COMMAND_OR_JUSTIFIED_NOT_APPLICABLE}} |
| Focused tests | {{FOCUSED_TEST_COMMAND}} |
| Full automated tests | {{FULL_TEST_COMMAND}} |
| Coverage generation and enforcement | {{COVERAGE_GATE_COMMAND}} |
| Build / packaging checks | {{BUILD_COMMAND}} |
| Dependency-boundary checks | {{ARCHITECTURE_CHECK_COMMAND_OR_CURRENT_LIMITATION}} |
| User-doc build, links, and examples | {{DOCS_COMMANDS_OR_JUSTIFIED_NOT_APPLICABLE}} |
| Fast aggregate | `scripts/check` |
| Full aggregate | `scripts/verify` |

Native tooling owns the implementation. Repository wrappers own the stable interface.
No automatic stack detector or universal build system is required.

## Formatting and static analysis

Use an established formatter for each implementation language where available.
Choose a meaningful linter/static-analysis ruleset for correctness, maintainability,
unsafe patterns, and applicable accessibility/security risks. Type-check typed code.

Check-only formatting and static analysis run in both validation paths. Formatting
fixes are a separate intentional developer action; verification must not rewrite code.
Do not disable rules broadly to get green. Suppressions need a concrete, local reason.
Avoid contradictory formatter/linter style rules and low-value cosmetic lint disputes.

## Source-size guard

Authored implementation and test source has a **300-line soft limit and a 500-line
hard ceiling**. Count physical lines, including comments and blank lines. Exactly
500 lines is permitted; 501 is a failure.

Above 300 lines, record a brief cohesion justification in the change/review record.
Decompose by responsibility, not arbitrary line slices. Do not minify, remove useful
comments, or add pass-through modules to game the ceiling.

Generated code, vendored sources, lockfiles, binaries, static assets, and build/test
outputs are excluded. Authored tests are not excluded. Tracked generated code needs
an explicit narrow exclusion; a broad exclusion for difficult code is not acceptable.
Documentation and prompt Markdown are not source-size-gated, but should remain concise.

`scripts/check-source-size.py` is the supplied deterministic guard. During adoption,
confirm its language/extensionless-source scope covers the project. Add languages
or generated-path exclusions explicitly in that script; do not silently omit sources.

## Coverage policy

Coverage is a diagnostic floor, not proof of completeness or a target to pad:

- ordinary testable production layers: **at least 80%**;
- explicitly identified core/critical production layers: **at least 90%**.

Assess risk, not folder names alone. Critical areas can include data integrity,
security boundaries, core algorithms, concurrency, protocol parsing, persistence,
real-time behavior, or other costly failure paths. Do not label everything critical
or move code to an ordinary group merely to pass a threshold.

Enforce thresholds per coherent layer/package/component, not only a repository
aggregate that can hide a weak core. Unit, component, and integration tests may all
contribute meaningful instrumented coverage; do not force isolated unit tests where
boundary tests provide better evidence.

Use line/statement coverage and branch coverage where the ecosystem supports a
reliable metric. Apply the declared floor to each selected metric; do not average
line and branch percentages. Record unsupported metrics explicitly. Do not invent
branch coverage or combine incomparable reports into a misleading number.

| Scope / included paths | Risk tier and rationale | Metrics / denominator | Floor | Native enforcement | Narrow exclusions |
|---|---|---|---|---|---|
| {{ORDINARY_COMPONENT}} | Ordinary: {{WHY}} | {{METRICS}} | 80% | {{CONFIG_AND_COMMAND}} | {{EXCLUSIONS_OR_NONE}} |
| {{CRITICAL_COMPONENT}} | Critical: {{WHY}} | {{METRICS}} | 90% | {{CONFIG_AND_COMMAND}} | {{EXCLUSIONS_OR_NONE}} |

Adapt or remove rows based on the actual system. Until this map and native coverage
gate exist, full verification is **unconfigured**, not passed. An applicable coverage
phase with missing reports, empty discovery, or zero tests must not silently succeed.
If there genuinely is no production code, explicitly document that coverage is not
applicable rather than pretending it is 100%.

Do not add execution-only assertions, excessive mocking, or tests whose primary goal
is a percentage. If a floor cannot be met honestly, report it and seek an explicit
policy decision. Do not lower it silently. Review material coverage loss even when
above the floor; there is no automatic ratchet requiring ever-increasing percentages.

## Behavior and boundary tests

For every reasonably testable defect, add a regression for the actual failure;
confirm it fails before the fix when practical. Document a concrete limitation when
such a test is infeasible. Preserve useful regressions unless the behavior is
intentionally removed or the test is demonstrably wrong/redundant.

Test success, invalid inputs, edge values, state transitions, ordering/identity,
partial failure, and recovery as material. Prefer realistic component/integration
boundaries over mocks that bypass the mechanism being verified.

For high-risk changes, exercise the consequence across the relevant boundary:
caller to service, database across restart, process to process, UI to backend, or
serialized data to consumer. Cover cancellation/races/resources where applicable.
Use deterministic seeds for generated cases; preserve a discovered failure as a
focused fixture. Add fuzzing/mutation tools only for a demonstrated unmet risk.

## Validation contract

`scripts/check` runs the shared fast phases and reports which full phases it omits.
`scripts/verify` runs all configured deterministic completion phases, using the same
phase definitions. Neither installs software, spends provider credits, publishes,
reformats, commits, or prompts interactively.

Both return nonzero on failure or missing required configuration/tooling. Fail fast
is acceptable; list unrun phases rather than suggesting they passed. Full verification
includes source size, formatting, static analysis, types where applicable, behavior
tests, coverage enforcement, build/package checks, architecture guards, and applicable
user-doc checks. Choose stack-specific implementations; do not duplicate pipelines.

CI should invoke the same authoritative gate after explicit environment setup.
Platform-dependent projects may run it per supported environment with a documented
matrix. Missing hardware/credentials or manual checks remain visible limitations;
a green local subset does not establish unsupported platform/live behavior.

## Review, acceptance, and Git

Implementation self-review and fresh independent review are distinct. Required fresh
review covers material concurrency, security, data-loss/migrations, state authority,
critical lifecycle/timing, or other high-risk behavior. Small low-risk changes need
proportionate review, not an automatic multi-agent ritual.

The operator initiates a separate reviewer or an explicitly authorized workflow does.
If required independent review is unavailable, implementation may be complete but
acceptance remains pending review. Another agent's summary is not evidence by itself.

For substantial changes: inspect the full diff, run full verification, resolve valid
findings, rerun affected gates after changes, update documentation, and record exact
remaining manual checks. Set finite acceptance criteria before testing; do not silently
expand the gate after every successful run or declare unperformed checks passed.

Default commit policy: **do not commit or push without operator authorization**.
When authorized, commit coherent verified milestones, review staged files, and preserve
pre-existing user changes. No force pushes, destructive cleanup, or deployment by default.

## User-facing documentation

User documentation is part of the product, not an implementation log. Update it in
the same change when users need to understand changed behavior, workflows, commands,
API/syntax, configuration, examples, limitations, compatibility, or recovery.

Provide first success, task-oriented guides, conceptual explanations where needed,
precise reference, and realistic troubleshooting. Document prerequisites, executable
examples, expected output/outcome, and recovery from meaningful errors. A beginner
should not need an internal design plan to use the product.

Authored content belongs in `docs/user/` when a larger guide is needed; a static
website can consume it later. Use the site's established structure if one already
exists rather than maintaining a duplicate content tree. Publish only intended public
content, never internal plans, agent transcripts, private evidence, or credentials.

Commands/snippets should be checked where practical. Generate implementation facts
from canonical definitions when that reduces drift, without building a generator for
trivial prose. Validate links, navigation, representative rendered pages, and examples.
A website build alone is not proof the instructions work.

Keep README as orientation and the shortest usable quick start. ARCHITECTURE describes
current structure; DESIGN describes UX guidance; accepted decisions preserve rationale;
feature plans/evidence preserve change history. Proposed features must be labelled as
proposed. Do not accumulate superseded reports in current user instructions.

## Completion record

A completion response records observable changes, exact commands and outcomes,
candidate revision plus uncommitted-work status, review disposition, docs impact,
and remaining limitations. Raw logs live in ignored run evidence; retain a concise
reviewable summary and relevant durable test fixtures. No fabricated test or UX evidence.
