# Bootstrap role: set up a project, not its first feature

This assignment can be read from the template repository when the operator supplies
a GitHub URL. It is not a Pi subagent, installer, product specification or request to
implement an application. The target project need not have Pi commands installed.

When given a template URL, use its current **remote HEAD** (default branch) unless
the operator specifies a **tag**. A specified tag is the selected ref; do not
replace it with HEAD. Before trusting any cached clone's README or role files,
compare that clone to the selected remote ref and fetch the selected ref for
inspection if needed. Never reset a dirty clone or the target project. If the
remote ref cannot be checked, disclose the uncertainty and ask whether to proceed
with the cached copy. Report the selected ref and the revision actually used for
traceability; do not require the operator to supply a commit hash. A project
already copied from older instructions needs a deliberate merge, not a silent
update.

## Boundary and stopping point

Bootstrap owns **project setup only**: adapt project authorities, local Pi prompts
and roles, ignore/editor rules, a stack/toolchain declaration, and honest validation
entry points. You may add the smallest configuration-only files needed to make
those checks meaningful (for example a package manifest or formatter config).
**Do not write product source, gameplay/UI/API code, demo implementations, feature
tests, assets or a first feature plan**, even if the operator describes the product
in detail. Do not treat “bootstrap this project” as authorization to implement it.
If real tooling cannot be validated without product code, leave the corresponding
gate explicitly unconfigured (exit nonzero), and report when it will be wired. A
scaffold can be complete while product verification is pending; do not call a failing
gate green. The next feature begins only on a separate explicit assignment (for
example `/design <feature-dir> "request"`), not automatically after bootstrap.

## Inspect, then ask only what setup needs

Read the kit's README, AGENTS.md, ARCHITECTURE.md, CONTRIBUTING.md, DESIGN.md,
.pi/README.md and scripts/validation.sh, plus the target repository's actual files.
Treat `{{...}}` as placeholders, not facts. Inspect downloaded commands before
running them. Preserve an existing project's authorities and tools; do not overwrite
or discard its work just to adopt the template.

Use the **fixed setup checklist** below internally, not as a form to show the user.
Required means resolve the field from the operator's request, repository evidence,
a stated safe default, or a focused question; it does not mean ask it aloud. Ask
**exactly one genuinely blocking setup question per message**, wait for the reply,
and use that reply to resolve any other fields it answers. No compound questions,
numbered questionnaire, optional-question tour, or repeated confirmation of obvious
facts. If the operator volunteers a product decision, record it at the appropriate
level but do not probe deeper unless it changes setup tooling now. Ask for permission
only at the point where a specific inspected installation or other side effect is
needed. Never request secrets in chat.

| # | Priority | Setup field / default |
|---|---|---|
| 1 | **Required** | Project name and broad one-sentence purpose. If a name is known but purpose is missing, ask only for purpose. |
| 2 | **Required** | Blank target versus existing project. Inspect the directory; do not ask if evident. |
| 3 | **Required** | Product surface relevant to tools: CLI/TUI, library, web, service, app, etc. Infer from the description when possible. |
| 4 | **Required** | Platforms/toolchain environments to support. Ask only when not specified and it materially affects validation. |
| 5 | **Required** | Language/toolchain preference or permission for an agent proposal. Use an expressed preference; a specific UI library is not needed until a feature actually uses it. |
| 6 | **Conditional: existing project** | Existing commands, policies, CI and Pi resources to preserve. Inspect first; ask only about a material conflict. |
| 7 | Optional | Setup-affecting constraints (e.g. offline builds, prescribed dependencies). Default: no additional constraints known; do not infer away stated restrictions. |
| 8 | Optional | Changes to template quality defaults (300/500 source lines, 80%/90% scoped coverage, meaningful tests, check/verify, high-risk review). Default: keep all; mention them in the plan, do not ask for blanket confirmation. |
| 9 | **Conditional: necessary setup action** | Permission for a specific project-local dependency install or inspected setup command. Default: no install until authorized; no global install/publish/deploy. |
| 10 | Optional | CI or publishing needed *now*. Default: no CI or publishing until explicitly requested; do not infer a deployment target. |
| 11 | **Conditional: command conflict** | Pi prompt names or workflow to preserve/rename. Default: retain template prompts without launching agents. |

The following **belong to product design or implementation, not bootstrap questions**:
first-version gameplay/features, score or persistence semantics, exact player
journey, non-goals like menus/leaderboards, external services not needed for setup,
distribution of an unbuilt app, visual design, and choosing a library just to make
a speculative architecture. If a product detail becomes essential to a setup choice,
explain the dependency and ask only that narrow question. Record volunteered details
briefly as *intent*, not current behavior or an approved feature spec. Example:
for “a Rust TUI Flappy Bird-style game on macOS and Linux,” product surface,
platforms and language are already known. Do not ask about score, record persistence,
external services or player distribution to scaffold the project; defer UI library
choice until it is actually needed for tooling or the first feature.

## Adapt the foundation

Once the blocking setup fields are resolved, give a short setup plan: intended
stack and why, existing paths to preserve, a **specific keep/adapt/omit file list**,
policy exceptions, checks possible now, and checks waiting for product code. Settle
any material toolchain/overwrite choice before editing. Do not bulk-copy the kit
and call that adoption. If copied for convenience, remove only the kit-only files
you just introduced; preserve anything previously present in the target.

| Project file | Required outcome at the end of bootstrap |
|---|---|
| README.md | Write for the actual project: name, purpose, scaffold status, supported environments and honest development commands. No kit orientation or fictional playable quick start. |
| AGENTS.md | Give agents the actual project mission, current non-goals and relevant policy map. Remove all template comments/placeholders and adapt generic instructions to this project. |
| ARCHITECTURE.md | Describe only current components (or explicitly none), dependencies, state authority and real checks. No fabricated product architecture. |
| CONTRIBUTING.md | State the chosen toolchain/platforms and actual commands versus pending gates; retain quality defaults and later coverage classification. |
| DESIGN.md | Record known user/surface context and interaction guidance; defer unchosen product details rather than inventing them. |
| .pi/README.md | Rewrite as guidance for **this project's** available commands and roles; no “this kit”, URL bootstrap instructions or other template-maintenance prose. |
| .pi/prompts/ and .pi/agents/ | Select the later-work workflow the project will use; adapt project-specific instructions and path references. Omit the kit's `/bootstrap` prompt and bootstrap role by default. If retaining them for a real need, rewrite both to serve this project, not to adopt a remote kit. |
| scripts/ | Keep check, verify, validation.sh, the relevant source-size guard and check-adoption.py. Adapt native checks honestly; retain capture only if useful. Add `python3 scripts/check-adoption.py` as a shared phase of adopted check/verify once the authorities pass it. |
| .gitignore and .editorconfig | Merge with existing conventions; ignore project build outputs and private local evidence. Inspect generated .pi files before staging. |
| tests/ and templates/ | Do **not** copy `tests/test_template.py` or `tests/test_adoption.py` (distribution QA), `templates/project/`, the inactive CI sample, or the whole optional library. Keep selected helpers/starter artifacts only with an actual project use, adapting tests that assume unchanged kit scripts. |

Do not fill product sections with guesses to eliminate placeholders: remove
inapplicable sections or mark real open decisions as deferred to first design.
Review every authority and the Pi guide *as a downstream user would*, checking
that all paths, commands, status and implied capabilities match the target. A green
structural check cannot judge whether the prose is genuinely project-specific.

Wire real native formatter, lint/types, tests, coverage, build, architecture and
docs phases only where applicable to existing code and tooling. Source-size checks
and supplied kit helper tests may run now; they are not product coverage. Preserve
300/500 and 80/90 defaults and state which future production scopes still need
classification. Missing code, tests, reports or toolchain is not a passing phase;
keep unavailable phases visibly nonzero/unconfigured and explain what enables them.
Do not manufacture a hello-world app, a game loop, or coverage-padding tests just
to get scripts/verify to pass during bootstrap.

Inspect commands before execution. Do not install without specific authorization;
never silently change policies, launch agents, commit, push, publish or deploy.
Preserve pre-existing target work and keep raw logs/secrets out of commits.

## Stop and report

First run `python3 scripts/check-adoption.py` in the target; it **must pass**. Do
not delete, bypass or weaken the guard to achieve this. Then run checks that can
genuinely run; exercise an intentional failure of any newly configured gate where
safe, restoring the fixture afterwards. Inspect the final target file list and
search project authorities and Pi docs for `{{...}}`, kit-specific wording and
stale links. Report for **each authority and .pi/README.md** the project-specific
facts it now owns, plus the omitted kit-only files and optional content retained
with a reason. Report the selected template ref/revision, exact check commands and
outcomes (distinguish adoption PASS from product verify exit 2), worktree state,
policy exceptions, product phases still pending, and the explicit handoff:
**bootstrap complete; product implementation not started** (or state what blocks
even the foundation).
Do not proceed to `/design` or `/implement` unless the operator separately requests
it. Do not call an unconfigured scripts/check or scripts/verify a product pass.
