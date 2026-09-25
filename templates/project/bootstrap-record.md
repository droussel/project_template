# Bootstrap completion: {{PROJECT_NAME}}

<!-- Copy as docs/bootstrap.md in the target project. This is an adoption record,
not a product roadmap. Mark each box only after performing the task and replace
its evidence marker with real paths, commands/results or decisions. An unavailable
product gate may be recorded as pending; it must not be described as passing. -->

Template ref: {{REMOTE_HEAD_OR_SELECTED_TAG}}
Template revision used: {{ACTUAL_RESOLVED_REVISION}}

- [ ] B1 Inspect target and selected template ref; preserve existing work. — Evidence: {{TARGET_STATUS_AND_TEMPLATE_REF}}
- [ ] B2 Resolve blocking setup choices; record defaults and deferred product decisions. — Evidence: {{SETUP_DECISIONS}}
- [ ] B3 Adapt all project authorities and .pi/README.md to the actual project. — Evidence: {{SIX_PROJECT_DOCUMENT_PATHS_AND_FACTS}}
- [ ] B4 Select useful Pi resources and scripts; omit kit-only content and local artifacts. — Evidence: {{KEPT_AND_OMITTED_PATHS}}
- [ ] B5 Configure honest validation and run available checks; list pending product phases. — Evidence: {{COMMANDS_RESULTS_AND_PENDING_GATES}}
- [ ] B6 Review final files, links and worktree; confirm no product implementation began. — Evidence: {{DIFF_OR_FILE_REVIEW_AND_STATUS}}

A checkmark is a claim backed by the evidence on that line. Do not mark a blocked
item complete. The adopted `scripts/check-adoption.py` must pass before calling the
foundation complete; product `scripts/verify` can still be unconfigured without
misrepresenting it as a pass. Keep this record brief and project-specific.
