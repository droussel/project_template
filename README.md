# Project Template

A reusable starting point for agent-assisted solo software development. It includes
project authorities, Pi prompts and role instructions, optional feature/user-doc
artifacts, and deterministic validation entry points. **It is a template kit, not
an application, installer or agent orchestrator.** It does not select your stack,
launch agents, install dependencies, or make an unconfigured build green.

## Bootstrap a new project with an agent

Start Pi in the **target** directory and give it an ordinary message:

> This is a new project. Use my project template at <repository URL> to bootstrap
> it. Read its README and `.pi/agents/bootstrap.md`; inspect this target first,
> then ask me the required setup questions before making consequential choices.

The one-sentence request with just the repository URL should also work: this README
is the entry point when an agent inspects the template. The agent may fetch or clone
the template for **inspection**, but must inspect downloaded commands before running
them, avoid overwriting existing target files, and ask before installing packages or
performing other unapproved side effects. You do not need `/bootstrap` in the target
before starting. A local `/bootstrap` prompt is included for use **after** the
resources are available; it runs in the current session and is not an installer.

The [bootstrap assignment](.pi/agents/bootstrap.md) contains the **fixed, numbered
26-question catalogue**, each marked Required, Conditional or Optional. The agent
should present it in one grouped form, prefilling verifiable facts as **proposed —
confirm** and showing defaults. Required answers can be “none” or “agent may
propose” where appropriate; undecided material choices become visible blockers, not
invented facts. Questions cover scope, users, platform/stack, integration, UX,
quality defaults, verification environments, Pi workflow, permissions and delivery.
The operator can answer several at once. Optional questions need not delay work.

The agent then summarizes the proposed product/stack, files to preserve or create,
policy exceptions and validation plan; settles material choices; adapts the project;
runs checks; and reports exact results and limitations. The supplied defaults remain
**300/500 physical source lines**, **80% ordinary / 90% critical per-layer coverage**,
meaningful regressions, a fast `check` and full `verify`, risk-based independent
review, no automatic delegation, and no commit/push without authorization. You may
explicitly change individual defaults during bootstrap; the agent must not silently
relax them. No production code means coverage is not yet applicable, not “100%”.

For an existing project, merge deliberately with its authorities, Pi resources,
scripts and CI; do not copy over them. Use only optional content that helps its
users. Replace this kit README with an adapted copy of
[the project README template](templates/project/README.md) in the target project.
Keep this README in the template repository for subsequent bootstraps.

### Bootstrap completion checklist

- The target's mission, scope, supported platforms and first-success instructions
  reflect real operator answers, not `{{...}}` placeholders or invented architecture.
- `AGENTS.md`, `ARCHITECTURE.md`, `CONTRIBUTING.md` and `DESIGN.md` agree with actual
  code and the selected stack; incompatible pre-existing instructions were resolved.
- `.pi/` contains only appropriate local prompts/roles, with paths and command names
  checked against existing Pi resources.
- Real formatter, static analysis, tests, coverage (where code exists), build,
  architecture and relevant docs phases are configured in the native tooling and
  exposed by `scripts/check` and `scripts/verify`; intentional failures are detected.
- The agent reports actual commands/results and unrun manual, provider, platform or
  CI checks. A pending decision or exit 2 is not a successful completed bootstrap.

## Authorities and included files

| Location | Responsibility |
|---|---|
| [AGENTS.md](AGENTS.md) | Downstream agent mission and operating rules; fill project placeholders. |
| [ARCHITECTURE.md](ARCHITECTURE.md) | Current system map and invariants, not proposed feature architecture. |
| [CONTRIBUTING.md](CONTRIBUTING.md) | Engineering policy, real stack/coverage map, verification and Git. |
| [DESIGN.md](DESIGN.md) | Product interactions; applicable to CLI/API ergonomics too. |
| [.pi/](.pi/README.md) | Pi prompt entry points and role instructions; not automatic subagents. |
| [templates/feature/](templates/feature/README.md) | Optional specification, reconnaissance, plan, review and handoff starters. |
| [templates/user-docs/](templates/user-docs/README.md) | Optional task-oriented public documentation starters. |
| [scripts/](scripts/validation.sh) | Shared check/verify dispatch, source-size guard and evidence capture. |

These are **templates** until adapted. Delete inapplicable sections rather than
inventing services or token systems. A proposed feature plan does not become current
architecture until accepted and implemented. Record important durable rationale in
[decision records](templates/decisions/decision.md) when warranted.

## Pi prompts and workflow

Project prompt templates in `.pi/prompts/` are available after Pi trusts a local
project and loads its resources; `/reload` picks up edits in an active session. Their
role files in `.pi/agents/` are plain Markdown read on demand. See [.pi/README.md](.pi/README.md)
for discovery, argument syntax and trust details. Quote paths/descriptions with
spaces; the prompts request missing arguments. They never open a fresh Pi session,
spawn an agent or switch models for you.

| Command | Purpose |
|---|---|
| `/bootstrap "description"` | Adapt a locally available kit into the current project. |
| `/design <feature-dir> "request"` | Specify desired behavior and acceptance criteria. |
| `/scout <feature-dir>` | Inspect actual repository mechanisms, write reconnaissance. |
| `/architecture <feature-dir>` | Draft an affected-boundaries plan for approval. |
| `/implement <feature-dir>` | Implement an approved bounded change and its regressions. |
| `/review <feature-dir> <base-ref>` | Review the actual candidate diff without source fixes. |
| `/specialist-review <feature-dir> <base-ref> "focus"` | Investigate one material risk. |
| `/docs <feature-dir> "task"` | Update and check user-facing documentation. |
| `/handoff <feature-dir>` | Persist compact, factual context for a next session. |

A substantial feature might use `docs/plans/active/midi-clock/`:

```text
/design docs/plans/active/midi-clock "Add MIDI clock support"
/scout docs/plans/active/midi-clock
/architecture docs/plans/active/midi-clock
# Operator reviews/approves scope and architecture; use fresh sessions if useful.
/implement docs/plans/active/midi-clock
# From a shell: scripts/verify
/review docs/plans/active/midi-clock <actual-base-ref>
# Operator evaluates findings; the implementer repairs accepted defects.
```

A small fix can instead use a direct change and regression. For independent context,
start another Pi session yourself and pass artifact paths rather than transcripts.
New tabs still share a checkout: assign exclusive write scope. Herdr can organize
sessions but is not required, and this kit supplies no launcher. Fresh independent
review is required for material high-risk behavior; implementation self-review is
not independent review. The operator owns approval and acceptance.

## Validation and evidence

```sh
scripts/check    # fast feedback; lists omitted full phases once adapted
scripts/verify   # full deterministic completion gate
python3 -m unittest discover -s tests -p 'test_*.py'  # kit tests, not product tests
```

Both wrappers use `scripts/validation.sh`. **As shipped, they deliberately return
exit 2** after the working Python source-size guard: stack formatter, lint, tests,
coverage, build, architecture and docs checks still need real wiring. Adapt shared
phases once to the stack's native tools; full verification is non-mutating, never
installs/publishes, and CI should call that same gate after explicit setup. Do not
turn an unconfigured phase into a successful no-op. Missing tests/reports must not
masquerade as passing coverage. Requires Bash 3.2+, Git and Python 3.9+; native
Windows support has not been established.

`check-source-size.py` checks Git-discovered authored source and tests: warning above
300 physical lines, failure above 500. Confirm language suffixes and narrow
generated-source exclusions when adopting a stack. For coverage, declare each
meaningful production scope, tier, supported metrics, denominator and native
threshold. See [CONTRIBUTING.md](CONTRIBUTING.md) for policy.

To save non-interactive command evidence without masking failures:

```sh
scripts/capture .agent-runs/example/001/verify -- scripts/verify
```

The directory must not already exist. Capture records output, exit status and Git
context; it is **not** a sandbox, redactor or test runner. `.agent-runs/` is ignored
by Git, but logs and command arguments can contain secrets; review before sharing.
Keep concise durable command summaries with the change, not raw private logs.

## Optional pieces and limits

Use [feature templates](templates/feature/README.md) proportionately, the optional
[design-system starter](templates/product/DESIGN_SYSTEM.md) only after real reusable
patterns exist, and [user-doc starters](templates/user-docs/README.md) where users
need more than a tested quick start. A later static site can publish `docs/user/`
without making the site an application dependency. The
[inactive CI template](templates/ci/verify.yml.template) needs a runner, pinned
actions and explicit toolchain setup before use. Choose a licence explicitly before
distribution; this kit chooses none.

No model defaults, provider credentials, global Pi settings, background agent
launcher, workflow database, or automatic deployment are included.
