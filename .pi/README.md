# Pi resources in this kit

`.pi/prompts/*.md` are project-scoped Pi prompt templates: the filename is a slash
command, available after Pi trusts the project and loads its resources (`/reload`
after edits in an active session). They expand text **in the current conversation**.
They do not create sessions, grant permission, install tooling, or launch agents.

`.pi/agents/*.md` are plain task-role instructions read by the corresponding
prompt. Pi does not discover these as autonomous subagents. An optional third-party
subagent extension could use its own agent-file convention, but this kit neither
ships nor configures one. Each role still follows AGENTS.md and project policies.

The initial URL-based bootstrap starts from an ordinary request in the **target**
project: read the template's root README and `.pi/agents/bootstrap.md`. Do not
expect the target to know `/bootstrap` before its resources have been copied. The
included `/bootstrap` is only a convenience when this kit is already local or the
prompt was copied into the project.

Prompt arguments use Pi's `$1`, `$2`, `$ARGUMENTS` and `${@:N}` expansions, with
shell-like quoting for paths/descriptions containing spaces. Missing required
arguments are requested by the prompt. `{{...}}` in project/artifact templates are
manual editing markers, not Pi variables. Prompts read role files **when invoked**;
they do not inline or magically load those files. The operator decides when to
start a separate session for context independence and avoids concurrent writes to
the same checkout.

Project resource names can conflict with user-level commands or extension commands;
inspect existing resources when adopting. Review unfamiliar project resources before
trusting them; project trust does not sandbox Pi's file/system access.

Upstream Pi references (check against the installed version):
- [Prompt templates](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/prompt-templates.md)
- [Configuration and context files](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/configuration.md)
- [Project trust and security](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/security.md)
