# User-documentation templates

These are content starters, not a website generator. Copy only useful pages into
`docs/user/` or the current site's established authored-content location. Do not
instantiate empty guides merely to complete a directory tree.

| Template | User need |
|---|---|
| `index.md` | Find the right entry point and understand the product. |
| `getting-started.md` | Achieve one real success with explicit prerequisites. |
| `how-to.md` | Complete a specific task efficiently. |
| `concept.md` | Understand a mental model needed for correct use. |
| `reference.md` | Look up exact syntax, configuration, API, defaults, or errors. |
| `troubleshooting.md` | Recognize a real failure and recover safely. |

Use clear user vocabulary, tested examples, expected results, and real limitations.
Do not publish plans or internal reports as user guidance. Keep generated reference
facts close to their canonical implementation when it actually reduces duplication.

A later static site may publish these pages to GitHub Pages, but no website build
is implied by these Markdown files. Keep authored pages in one authoritative
location (`docs/user/` if there is no existing convention); publish only explicitly
selected public content, never plans, raw `.agent-runs/` evidence or secrets.
Choose the generator, navigation, base path and deployment permissions for the
actual project. Verify links, representative rendered pages, first-success commands
and recovery instructions; a site build alone does not prove the instructions work.
