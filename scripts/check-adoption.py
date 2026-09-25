#!/usr/bin/env python3
"""Check a downstream project for unadapted project-template material.

This is a structural guard, not a review of whether project policies are sensible.
The kit itself intentionally fails; run on an adopted project after customization.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from urllib.parse import unquote

AUTHORITIES = (
    'README.md', 'AGENTS.md', 'ARCHITECTURE.md', 'CONTRIBUTING.md',
    'DESIGN.md', '.pi/README.md',
)
REQUIRED_SCRIPTS = ('scripts/check', 'scripts/verify', 'scripts/validation.sh',
                    'scripts/check-adoption.py')
KIT_ONLY = (
    'tests/test_template.py',
    'tests/test_adoption.py',
    'templates/project/README.md',
    'templates/project/bootstrap-record.md',
    'templates/ci/verify.yml.template',
    'template-guide',
)
WHOLESALE_SETS = (
    ('feature artifacts', ('templates/feature/README.md',
                           'templates/feature/feature-spec.md',
                           'templates/feature/architecture.md',
                           'templates/feature/review.md')),
    ('user-documentation starters', ('templates/user-docs/README.md',
                                     'templates/user-docs/getting-started.md',
                                     'templates/user-docs/reference.md')),
)
UNADAPTED_FRAGMENTS = {
    'README.md': ('# Project Template', 'template kit, not'),
    '.pi/README.md': ('# Pi resources in this kit', 'this kit neither',
                      'when this kit is already local'),
    '.pi/prompts/bootstrap.md': ('Adapt this template kit',
                                  'Read `.pi/agents/bootstrap.md` and the root README'),
    '.pi/agents/bootstrap.md': ('# Bootstrap role: set up a project, not its first feature',),
}
PLACEHOLDER = re.compile(r'\{\{[^{}\n]+\}\}')
CHECKLIST = (
    'Inspect target and selected template ref; preserve existing work.',
    'Resolve blocking setup choices; record defaults and deferred product decisions.',
    'Adapt all project authorities and .pi/README.md to the actual project.',
    'Select useful Pi resources and scripts; omit kit-only content and local artifacts.',
    'Configure honest validation and run available checks; list pending product phases.',
    'Review final files, links and worktree; confirm no product implementation began.',
)


def check_record(root: Path) -> list[str]:
    name = 'docs/bootstrap.md'
    path = root / name
    if not path.is_file():
        return [f'{name}: missing bootstrap completion record']
    try:
        text = path.read_text(encoding='utf-8')
    except (OSError, UnicodeError) as exc:
        return [f'{name}: cannot read UTF-8 text: {exc}']
    errors: list[str] = []
    if PLACEHOLDER.search(text) or 'Copy as docs/bootstrap.md' in text:
        errors.append(f'{name}: unfilled starter content')
    if not re.search(r'(?m)^Template ref: \S.+$', text):
        errors.append(f'{name}: missing selected HEAD or tag')
    if not re.search(r'(?m)^Template revision used: [0-9a-f]{7,40}$', text):
        errors.append(f'{name}: missing resolved template revision')
    seen: set[str] = set()
    for line in text.splitlines():
        if not re.match(r'^\s*[-*]\s*\[', line):
            continue
        item = re.fullmatch(r'- \[([ xX])\] (B\d+) (.*?) — Evidence: (.*)', line)
        if item is None:
            errors.append(f'{name}: malformed checklist item: {line}')
            continue
        mark, identifier, label, evidence = item.groups()
        if identifier in seen:
            errors.append(f'{name}: duplicate task {identifier}')
        seen.add(identifier)
        if not identifier[1:].isdigit() or int(identifier[1:]) not in range(1, len(CHECKLIST) + 1):
            errors.append(f'{name}: unexpected task {identifier}')
            continue
        if label != CHECKLIST[int(identifier[1:]) - 1]:
            errors.append(f'{name}: changed task description {identifier}')
        if mark != 'x':
            errors.append(f'{name}: unchecked task {identifier}')
        if len(evidence.strip()) < 10 or PLACEHOLDER.search(evidence) or evidence.strip().lower() in {'done', 'n/a', 'pending'}:
            errors.append(f'{name}: missing concrete evidence for {identifier}')
    for number in range(1, len(CHECKLIST) + 1):
        if f'B{number}' not in seen:
            errors.append(f'{name}: missing task B{number}')
    return errors


def check(root: Path) -> list[str]:
    errors: list[str] = []
    errors.extend(check_record(root))
    for name in AUTHORITIES:
        path = root / name
        if not path.is_file():
            errors.append(f'{name}: missing project authority')
            continue
        try:
            text = path.read_text(encoding='utf-8')
        except (OSError, UnicodeError) as exc:
            errors.append(f'{name}: cannot read UTF-8 text: {exc}')
            continue
        if not text.strip():
            errors.append(f'{name}: empty project authority')
        if PLACEHOLDER.search(text) or '<!-- TEMPLATE:' in text:
            errors.append(f'{name}: unfilled template marker')
        for fragment in UNADAPTED_FRAGMENTS.get(name, ()):
            if fragment in text:
                errors.append(f'{name}: still describes the template kit ({fragment!r})')
        for target in re.findall(r'(?<!!)\[[^]]+\]\(([^)]+)\)', text):
            if target.startswith(('https://', 'http://', 'mailto:', '#', '/')):
                continue
            path_part = unquote(target.split('#', 1)[0].split('?', 1)[0])
            if path_part and not (path.parent / path_part).exists():
                errors.append(f'{name}: broken local link: {target}')

    for name in REQUIRED_SCRIPTS:
        if not (root / name).is_file():
            errors.append(f'{name}: missing validation entry point')
    validation = root / 'scripts/validation.sh'
    if validation.is_file():
        try:
            lines = validation.read_text(encoding='utf-8').splitlines()
            if not any('scripts/check-adoption.py' in line for line in lines
                       if line.strip() and not line.lstrip().startswith('#')):
                errors.append('scripts/validation.sh: adoption guard not wired as a phase')
        except (OSError, UnicodeError) as exc:
            errors.append(f'scripts/validation.sh: cannot read UTF-8 text: {exc}')
    prompts = root / '.pi/prompts'
    if not prompts.is_dir() or not list(prompts.glob('*.md')):
        errors.append('.pi/prompts/: no project workflow prompts')
    else:
        for prompt in prompts.glob('*.md'):
            try:
                text = prompt.read_text(encoding='utf-8')
            except (OSError, UnicodeError) as exc:
                errors.append(f'{prompt.relative_to(root)}: cannot read UTF-8 text: {exc}')
                continue
            for role in re.findall(r'\.pi/agents/[a-zA-Z0-9_-]+\.md', text):
                if not (root / role).is_file():
                    errors.append(f'{prompt.relative_to(root)}: missing role {role}')

    for name in KIT_ONLY:
        if (root / name).exists():
            errors.append(f'{name}: kit-only material copied into the project')
    for label, names in WHOLESALE_SETS:
        if all((root / name).is_file() for name in names):
            errors.append(f'templates/: wholesale {label}; select only needed starters')
    for name in ('.pi/prompts/bootstrap.md', '.pi/agents/bootstrap.md'):
        path = root / name
        if path.is_file():
            try:
                text = path.read_text(encoding='utf-8')
            except (OSError, UnicodeError) as exc:
                errors.append(f'{name}: cannot read UTF-8 text: {exc}')
                continue
            if any(fragment in text for fragment in UNADAPTED_FRAGMENTS[name]):
                errors.append(f'{name}: kit bootstrap role/prompt not removed or rewritten')

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    root = parser.parse_args().root.resolve()
    if not root.is_dir():
        print(f'ERROR: no directory: {root}', file=sys.stderr)
        return 2
    errors = check(root)
    for error in errors:
        print(f'FAIL: {error}', file=sys.stderr)
    if errors:
        print(f'Adoption: {len(errors)} issue(s). Resolve them before claiming bootstrap complete.',
              file=sys.stderr)
        return 1
    print('Adoption structure: PASS. Review each authority for project-specific truth.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
