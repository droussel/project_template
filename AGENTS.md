# Agent Instructions

<!-- TEMPLATE: customize the mission and project map before substantial product work.
Keep this file concise; detailed engineering policy belongs in CONTRIBUTING.md. -->

## Mission

{{PROJECT_PURPOSE_AND_PRIMARY_USER_OUTCOME}}

Out of scope: {{EXPLICIT_NON_GOALS}}

Until these sections and validation commands are configured, this repository is a
template, not evidence of an implemented product. Template adoption is a legitimate
first task; do not create fictional architecture to fill blanks. If the current
assignment is bootstrap, follow `.pi/agents/bootstrap.md`: set up the foundation
only. A product description is not permission to implement its first feature.

## Read the relevant authority

- `ARCHITECTURE.md`: current components, dependencies, ownership, and hard invariants.
- `CONTRIBUTING.md`: engineering, coverage, source-size, verification, review, and docs policy.
- `DESIGN.md`: product interaction guidance for user/developer-facing changes.
- The active feature specification, approved architecture, and applicable accepted decisions.
- Existing subsystem or user documentation relevant to the actual change.

Read proportionately. Do not ingest every role prompt, historical plan, or document
for every task. A role prompt defines a task procedure; it does not override project
truth or a more specific authorized assignment.

Do not treat examples, template placeholders, proposed designs, or an agent's
summary as established facts. Distinguish current implementation, intended behavior,
and observed discrepancies.

## Scope and autonomy

Proceed through safe, authorized implementation, focused verification, self-review,
and documentation without asking permission for every small step.

Choose the smallest complete, architecture-consistent change. Extend an existing
cohesive mechanism before introducing a parallel one. New modules, abstractions,
configuration, dependencies, or extension points need a current requirement or a
specific invariant. Avoid adjacent cleanup and speculative extensibility.

Resolve minor ambiguities from the explicit task, accepted decisions, architecture,
existing conventions, then the simplest reversible choice. Record material choices
in the feature artifact. Escalate when user behavior would materially differ,
a hard-to-reverse decision is unresolved, scope materially expands, or required
credentials, hardware, permission, or information are unavailable.

Never silently weaken a test, policy, validation gate, or architectural invariant
to make an implementation pass.

## Planning and handoffs

Use a feature spec and architecture/implementation plan for substantial, unfamiliar,
cross-layer, or high-risk work. Use `templates/feature/` as needed, not as a mandatory
form for a trivial change.

Persist an approved planning result before an implementation handoff. If the session
is read-only, return the proposed text and identify the intended path; do not claim
it was saved. A chat transcript is not the sole durable implementation specification.

Architectural plans must cover all affected layers, boundary contracts, state and
failure semantics, verification, and delivery order. Private helpers and reversible
local choices may remain with the implementer. Material uncertainty remains visible.

Record a decision separately only when its rationale is durable, cross-cutting, or
expensive to reverse. Update current architecture after an accepted change actually
alters it; do not paste feature plans into `ARCHITECTURE.md`.

## Agents and context economy

The operator chooses models, starts sessions, and authorizes any workflow launcher.
Do not launch, delegate to, or commission another agent unless explicitly authorized
for the current assignment. Role files do not themselves authorize delegation.

Use one coherent implementation assignment rather than fragmenting investigation,
editing, tests, debugging, and self-review across agents. Preserve useful context
for ordinary repairs. Use a fresh independent reviewer when the risk requires it;
never describe self-review as independent review.

Keep responsibilities and write ownership explicit. Do not permit overlapping source
edits just because agents are in separate tabs. Handoff approved artifacts and
specific evidence, not entire transcripts or duplicated repository exploration.

## Verification and honesty

`scripts/check` is fast feedback. `scripts/verify` is the authoritative deterministic
completion gate. Their phase definitions belong in one shared implementation.

During development, run focused tests. Before claiming substantial product work complete,
run full verification, inspect the complete diff, evaluate required review findings,
update relevant durable/user documentation, and record any manual evidence still
needed. After changes, rerun checks whose evidence is no longer valid. A code-free
bootstrap may finish with product phases still unconfigured, but must report them
as pending and must not claim product verification passed.

Every reasonably testable defect needs a meaningful regression. Coverage floors,
file-size limits, formatter/linter configuration, and risk-based review rules live in
`CONTRIBUTING.md`; do not restate or improvise them here.

Report exact commands, results, tested revision/worktree, relevant limitations, and
remaining blockers. Distinguish not run, unavailable, failed, and passed. A successful
build, a file's existence, or an agent's “done” response is not behavioral acceptance.

## Safety and Git

Inspect status before changes; preserve pre-existing user work. Do not reset, clean,
stash, overwrite, delete, install globally, publish, or modify unrelated files without
explicit authorization. Keep secrets, private transcripts, and raw sensitive logs out
of commits and public documentation.

The project commit policy is set in `CONTRIBUTING.md`. The default is no commit or
push without operator authorization. When authorized, commit coherent verified
milestones, inspect the staged diff, and exclude local/generated artifacts. A dirty
tree is not permission to discard changes.

## User-facing changes

Read `DESIGN.md`, inspect the existing experience, and establish the user task,
important states, information hierarchy, and keyboard/accessibility behavior before
substantial UI work. Follow an established design system when one exists; do not
invent one merely to satisfy a template.

Check rendered behavior and real interaction, not screenshots or compilation alone.
Use a specialist only when the operator authorizes one for a material design question.

## Documentation and completion response

User guidance changes with user-visible behavior, commands, APIs, configuration,
examples, compatibility, and recovery procedures. Follow `CONTRIBUTING.md` and the
project's existing documentation organization.

Conclude with changed behavior, affected files, verification evidence, unresolved
findings or manual checks, and the next necessary action. Do not automatically start
the next workflow stage or promise background work.
