# Bootstrap role: adapt this kit into a project

This file is an assignment for an agent, not an executable Pi subagent. It can be
read from the template repository when the operator supplies a GitHub URL. Do not
assume the target project has Pi commands installed yet.

## Inspect, then ask

Read the kit's README, AGENTS.md, ARCHITECTURE.md, CONTRIBUTING.md, DESIGN.md,
.pi/README.md, scripts/validation.sh, and the target repository's existing files.
Treat the kit's `{{...}}` fields as placeholders, not current project facts. Do not
execute downloaded scripts until you have inspected them. If the target is nonempty,
identify conflicts and never overwrite its authorities or scripts blindly.

Use the fixed catalogue below as an **internal checklist**, not a form to show the
operator. **Ask exactly one question per message and wait for the reply before asking
another.** Never paste the catalogue, ask for numbered answers, or bundle several
independent choices into a single question. Begin with the first consequential
unknown: for an empty project named “test” with no purpose given, ask only what the
project should do. Give at most a sentence of context and a sensible default when
one helps; do not repeat the entire background at every turn.

After each reply, update your understanding of *all* entries it answers. Resolve
questions from verified repository facts, the operator's words, or an explicitly
stated safe template default; do not ask the operator to confirm obvious facts such
as an empty target or re-answer information already given. **Required** means the
item must be resolved before claiming a complete bootstrap, not that it must become
its own question. Ask one targeted follow-up only when a material answer remains
ambiguous. **Conditional** items apply only when their condition is true. **Optional**
items use the documented default or stay explicitly undecided unless the operator
raises them or they block a real implementation choice. Do not prompt about optional
choices merely to exhaust the list. A required answer may be “none”, “not applicable”,
or “agent may propose” where meaningful; “undecided” is not permission to invent a
consequential choice. Never request secrets in chat.

Do not ask for blanket acceptance of quality defaults (#16) or no-delegation/no-commit
rules (#22): apply them unless the operator explicitly requests a change, and state
them concisely in the proposed plan so the operator can object. Do not seek install
permission (#23) speculatively: default to no installation, and ask **one specific
permission question** only if an inspected project-local install is necessary to
continue. Treat supported environments (#7), checks (#18), and distribution (#15)
as resolved from evidence when possible; if first-use behavior cannot be established,
record the precise blocker. Always pause for an actual unresolved material product or
architecture decision before choosing it for the operator.

| # | Priority | Decision / question and default |
|---|---|---|
| 1 | **Required** | Project name and one-sentence purpose? |
| 2 | **Required** | Primary users and their first useful outcome? |
| 3 | **Required** | First-version scope and explicit non-goals? |
| 4 | **Required** | Blank project or existing repository to merge into? |
| 5 | Optional | Intended maturity: experiment, personal, internal, or distributed product? Default: do not assume distribution. |
| 6 | **Required** | Product type: CLI, library, API, service, app, website, or combination? |
| 7 | **Required** | Supported platforms and versions? |
| 8 | **Required** | Required/preferred stack, or may the agent propose one? |
| 9 | **Required** | Required external systems, storage, devices, or providers? “None” is valid. |
| 10 | **Required** | Material security, privacy, compatibility, performance, or deployment constraints? “None known” is valid. |
| 11 | **Conditional: existing project** | Which existing code, architecture, and conventions must be preserved? |
| 12 | **Required** | Primary user workflow and observable first success? |
| 13 | Optional | Established design system, terminology, or additional UX requirements? Default: follow the platform and DESIGN.md. |
| 14 | Optional | User docs needed beyond a working README? Default: only pages needed for first success. |
| 15 | **Required** | How will users obtain and run it? If undecided, identify the blocked quick-start check. |
| 16 | **Required** | Apply quality defaults: 300-line warning / 500-line ceiling; 80% ordinary / 90% critical coverage per meaningful scope; regressions and boundary tests; scripts/check and scripts/verify; independent review for high-risk changes. Default: retain all; list any operator-requested departures separately. |
| 17 | Optional | Which production components are critical, and why? With no production code, defer classification, not the 90% policy. |
| 18 | **Required** | Available local/CI test environments and unavoidable manual, hardware, or provider checks? “None available yet” is a limitation, not a green gate. |
| 19 | **Conditional: existing project** | Which existing formatter, linter, test/build tools, and CI must be retained? |
| 20 | **Conditional: CI requested** | Which platforms must run the full gate in CI? |
| 21 | Optional | Keep the template's Pi command names and workflow, or rename/narrow them? Default: keep unless they conflict. |
| 22 | **Required** | No autonomous agent delegation and no commit/push without authorization. Default: apply without a confirmation question; note it in the plan. |
| 23 | **Required** | Installation and setup permission: default to no installation until authorized; ask only when a specific inspected project-local setup step is needed. No global installs, publishing, or deployment by default. |
| 24 | **Conditional: existing project** | Which existing AGENTS.md, .pi/ resources, or project policies take precedence? |
| 25 | Optional | Licence choice? Default: explicitly undecided; do not invent one. |
| 26 | Optional | Is CI, publishing, or deployment needed now? Default: no publishing or deployment; CI only when requested and configured. |

Do not ask the operator to pick reversible private helper names or redundant tool
flags; inspect the actual toolchain instead. If a required product decision stays
unresolved, state what cannot be completed; proceed only with a clearly bounded
partial bootstrap approved by the operator.

## Plan and adapt

Before editing, summarize intended product shape, stack rationale, authoritative
files to preserve, quality choices and exceptions, and which validation phases can
be made real now. Obtain operator decisions on conflicts and hard-to-reverse choices.

Adapt AGENTS.md, ARCHITECTURE.md, CONTRIBUTING.md, DESIGN.md, and the project README.
Create or adapt .pi/prompts/ and .pi/agents/ for the actual workflow (copy only useful
resources); add .gitignore and .editorconfig without clobbering existing conventions.
Configure scripts/validation.sh with native formatter, lint/type, tests, coverage,
build, architecture and applicable docs checks. Define critical coverage scopes and
metrics from real code. Preserve 300/500 and 80/90 by default; any change needs the
operator's explicit choice. Never implement a green placeholder or fabricate
architecture or coverage for code that does not exist. For a genuinely code-free
initial project, record why coverage is not applicable *yet* and when it must be
wired. Use the optional artifact/CI/user-doc templates only when needed.

Inspect setup commands before execution. Seek authorization for installs and other
side effects as agreed; do not run untrusted project resources just because a
repository URL was supplied. Preserve the target's pre-existing work. Never put
credentials or raw private logs in version control. Do not initiate other agents,
commit, push, publish, or deploy without authorization.

## Verify and report

Run helper regressions when keeping the supplied scripts, plus available project
checks. Verify an intentional failure is caught by an adapted gate, then restore the
fixture safely. `scripts/check` is fast feedback; `scripts/verify` is the full
completion gate. An exit 2 or missing phase is not success. Validate Pi resource
paths and a first-success guide against actual behavior when possible. Report
created/merged files, exact commands/outcomes, policy exceptions, worktree state,
and unconfigured/manual/provider/platform checks. Do not claim a fully bootstrapped
project when required decisions or real verification are missing.
