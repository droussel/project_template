#!/usr/bin/env python3
"""Check authored source size; use Git for scope, never traverse outside the repo.

Exit 0: checked files are <=500 physical lines (301+ warns).
Exit 1: at least one hard-limit violation.
Exit 2: invalid invocation, discovery, or unreadable/undecodable source.
Generated tracked files may be excluded explicitly below; do not exclude tests.
"""
from __future__ import annotations

import argparse
import fnmatch
import subprocess
import sys
from pathlib import Path

SOFT_LIMIT = 300
HARD_LIMIT = 500
SOURCE_SUFFIXES = {
    '.rs', '.py', '.pyi', '.ts', '.tsx', '.js', '.jsx', '.mjs', '.cjs',
    '.css', '.scss', '.sass', '.go', '.java', '.kt', '.kts', '.swift',
    '.c', '.h', '.cc', '.cpp', '.cxx', '.hpp', '.hxx', '.cs', '.rb',
    '.sh', '.bash', '.zsh', '.ps1', '.psm1', '.astro', '.vue', '.svelte',
    '.php', '.sql', '.ex', '.exs', '.erl', '.hrl', '.clj', '.cljs',
    '.lua', '.dart', '.m', '.mm', '.fs', '.fsx', '.f90', '.jl', '.r',
}
# Repository-relative shell-style globs for TRACKED generated/vendor sources only.
# Add a comment explaining the generator/vendor and why authored code cannot match.
# Git already omits ignored untracked build/vendor outputs.
EXCLUDED_PATHS: tuple[str, ...] = ()
SPECIAL_SOURCE_NAMES = {'Makefile', 'Dockerfile', 'Justfile', 'justfile'}


def discover(root: Path) -> list[Path]:
    result = subprocess.run(
        ['git', '-C', str(root), 'ls-files', '--cached', '--others',
         '--exclude-standard', '-z', '--', '.'],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False,
    )
    if result.returncode:
        message = result.stderr.decode('utf-8', errors='replace').strip()
        raise RuntimeError(f'Git discovery failed. Initialize/adopt a Git repo first. {message}')
    names = sorted(set(result.stdout.decode('utf-8').split('\0')) - {''})
    paths = []
    for name in names:
        candidate = root / name
        # Deleted tracked paths do not belong to the current worktree.
        if candidate.is_symlink():
            print(f'SKIP symlink (not followed): {name}')
            continue
        if not candidate.exists():
            continue
        if not candidate.is_file():
            continue  # e.g. a submodule: validate it through its own native gate.
        if not candidate.resolve().is_relative_to(root):
            raise RuntimeError(f'Refusing path outside repository scope: {name}')
        if any(fnmatch.fnmatchcase(name, pattern) for pattern in EXCLUDED_PATHS):
            print(f'SKIP explicit generated/vendor exclusion: {name}')
            continue
        suffix = candidate.suffix.lower()
        extensionless_script = not suffix and 'scripts' in candidate.relative_to(root).parts
        if suffix in SOURCE_SUFFIXES or candidate.name in SPECIAL_SOURCE_NAMES or extensionless_script:
            paths.append(candidate)
    return paths


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1],
                        help='Repository/subtree root (defaults to the template project).')
    args = parser.parse_args()
    root = args.root.resolve()
    if not root.is_dir():
        print(f'ERROR: no directory: {root}', file=sys.stderr)
        return 2
    try:
        paths = discover(root)
        failures = 0
        warnings = 0
        for path in paths:
            # Physical lines, including blank lines and comments, with or without final LF.
            text = path.read_text(encoding='utf-8')
            count = len(text.splitlines())
            relative = path.relative_to(root).as_posix()
            if count > HARD_LIMIT:
                failures += 1
                print(f'FAIL {relative}: {count} lines (maximum {HARD_LIMIT})', file=sys.stderr)
            elif count > SOFT_LIMIT:
                warnings += 1
                print(f'WARN {relative}: {count} lines; record a cohesion rationale.')
        print(f'Source size: {len(paths)} authored files; {warnings} warnings; {failures} failures.')
        return 1 if failures else 0
    except (OSError, UnicodeError, RuntimeError) as error:
        print(f'ERROR: {error}', file=sys.stderr)
        return 2


if __name__ == '__main__':
    sys.exit(main())
