# Feature artifacts

Copy only what the current change needs into one explicit directory, usually
`docs/plans/active/<feature>/`. These are ordinary Markdown documents, not machine
workflow state or approval gates. Do not create every document for a one-line fix.

| File | Use |
|---|---|
| `feature-spec.md` | Intent, behavior, constraints, non-goals, and acceptance criteria. |
| `reconnaissance.md` | Repository facts collected for a separate architect. |
| `architecture.md` | Proposed change, affected layers, contracts, risks, and delivery sequence. |
| `implementation-notes.md` | Actual changes, deviations, and verification summary. |
| `review.md` | Evidence-backed findings and their later disposition. |
| `handoff.md` | Small context packet for the next independently started session. |
| `sessions.md` | Optional pointers to Pi session IDs/usage logs; no copied telemetry database. |

Raw command output belongs in ignored `.agent-runs/<feature>/<attempt>/`. Link it
from a concise durable summary; promote only sanitized evidence or regression fixtures
that future readers actually need. A local file link is not durable archival evidence
unless its target is intentionally retained somewhere accessible.

When a feature is complete, move the useful document set to
`docs/plans/completed/<feature>/` if the project uses that convention. Update current
architecture/design/user docs separately. Do not keep proposed behavior as current truth.

Placeholders `{{...}}` are explicit editing instructions. Fill or remove them; no
renderer or substitution engine consumes them. Preserve exact criterion IDs in
references; put explanatory text in a separate field rather than renaming an ID.
