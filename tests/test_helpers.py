#!/usr/bin/env python3
"""Optional, standard-library-only tests for the supplied template shell helpers.

Run: python3 tests/test_helpers.py
These test the kit, not an adopted project's native code or coverage policy.
"""
from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SOURCE = Path(__file__).resolve().parents[1]


class HelperTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='project-template-test-')
        self.root = Path(self.temp.name) / 'project with spaces'
        self.root.mkdir()
        shutil.copytree(SOURCE / 'scripts', self.root / 'scripts')
        (self.root / '.gitignore').write_text('.agent-runs/\nnode_modules/\n')
        self.assertEqual(self.run_command('git', 'init', '-q').returncode, 0)

    def tearDown(self):
        self.temp.cleanup()

    def run_command(self, *args):
        return subprocess.run(args, cwd=self.root, capture_output=True, text=True, timeout=10)

    def file(self, name, text):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text)
        return path

    def guard(self):
        return self.run_command(sys.executable, 'scripts/check-source-size.py')

    def wire(self, fast, full):
        path = self.root / 'scripts/validation.sh'
        text = path.read_text().replace(
            "  unconfigured 'stack fast phases: formatter, static analysis, types, fast tests'", fast
        ).replace(
            "  unconfigured 'stack full phases: full tests, coverage, build, architecture, documentation'", full
        )
        path.write_text(text)

    def test_shell_syntax(self):
        for name in ('check', 'verify', 'validation.sh', 'capture'):
            result = self.run_command('bash', '-n', f'scripts/{name}')
            self.assertEqual(result.returncode, 0, result.stderr)

    def test_source_soft_boundary(self):
        self.file('src/item.ts', '// line\n' * 300)
        result = self.guard()
        self.assertEqual(result.returncode, 0)
        self.assertNotIn('WARN', result.stdout)
        self.file('src/item.ts', '// line\n' * 301)
        self.assertIn('WARN src/item.ts', self.guard().stdout)

    def test_source_hard_boundary(self):
        self.file('src/item.rs', '// line\n' * 500)
        self.assertEqual(self.guard().returncode, 0)
        self.file('src/item.rs', '// line\n' * 501)
        self.assertEqual(self.guard().returncode, 1)

    def test_tests_included_docs_and_ignored_excluded(self):
        self.file('docs/guide.md', 'line\n' * 800)
        self.file('node_modules/ignored.js', '// line\n' * 800)
        self.assertEqual(self.guard().returncode, 0)
        self.file('tests/large.test.ts', '// line\n' * 501)
        self.assertEqual(self.guard().returncode, 1)

    def test_symlink_is_not_followed(self):
        outside = Path(self.temp.name) / 'outside.py'
        outside.write_text('# line\n' * 800)
        (self.root / 'linked.py').symlink_to(outside)
        result = self.guard()
        self.assertEqual(result.returncode, 0)
        self.assertIn('SKIP symlink', result.stdout)

    def test_unconfigured_gates_fail(self):
        for name in ('check', 'verify'):
            result = self.run_command('bash', f'scripts/{name}')
            self.assertEqual(result.returncode, 2)
            self.assertIn('UNCONFIGURED', result.stderr)

    def test_failed_command_inside_function_is_not_masked(self):
        self.wire("  bash -c 'exit 7'\n  touch should-not-exist", '  touch full-not-run')
        result = self.run_command('bash', 'scripts/verify')
        self.assertEqual(result.returncode, 7, result.stdout + result.stderr)
        self.assertFalse((self.root / 'should-not-exist').exists())
        self.assertFalse((self.root / 'full-not-run').exists())

    def test_common_and_full_phases(self):
        self.wire("  printf 'fast\\n' >> phases.log", "  printf 'full\\n' >> phases.log")
        result = self.run_command('bash', 'scripts/check')
        self.assertEqual(result.returncode, 0)
        self.assertIn('CHECK ONLY', result.stdout)
        result = self.run_command('bash', 'scripts/verify')
        self.assertEqual(result.returncode, 0)
        self.assertEqual((self.root / 'phases.log').read_text(), 'fast\nfast\nfull\n')

    def test_capture_success_and_combined_output(self):
        result = self.run_command('bash', 'scripts/capture', '.agent-runs/ok', '--',
                                  'bash', '-c', 'echo stdout; echo stderr >&2')
        self.assertEqual(result.returncode, 0, result.stderr)
        output = (self.root / '.agent-runs/ok/output.log').read_text()
        self.assertIn('stdout', output)
        self.assertIn('stderr', output)

    def test_capture_failure_preserves_exit(self):
        result = self.run_command('bash', 'scripts/capture', '.agent-runs/fail', '--',
                                  'bash', '-c', 'exit 42')
        self.assertEqual(result.returncode, 42)
        status = (self.root / '.agent-runs/fail/status.txt').read_text()
        self.assertIn('FAILED', status)

    def test_capture_never_overwrites_an_attempt(self):
        keep = self.file('.agent-runs/old/notes.txt', 'keep')
        result = self.run_command('bash', 'scripts/capture', '.agent-runs/old', '--', 'true')
        self.assertEqual(result.returncode, 2)
        self.assertEqual(keep.read_text(), 'keep')

    def test_missing_command_is_failure(self):
        result = self.run_command('bash', 'scripts/capture', '.agent-runs/missing', '--',
                                  'template-helper-command-does-not-exist')
        self.assertEqual(result.returncode, 127)


if __name__ == '__main__':
    unittest.main(verbosity=2)
