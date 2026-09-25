#!/usr/bin/env python3
"""Regression tests for the downstream adoption guard, not product behavior."""
from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

KIT = Path(__file__).resolve().parents[1]
GUARD = KIT / 'scripts/check-adoption.py'


class AdoptionGuardTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='adoption-test-')
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for name in ('README.md', 'AGENTS.md', 'ARCHITECTURE.md',
                     'CONTRIBUTING.md', 'DESIGN.md', '.pi/README.md'):
            self.file(name, '# Jumping Potato\n\nProject-specific status and policy.\n')
        self.file('.pi/prompts/design.md', '---\ndescription: Design feature\n---\n')
        for name in ('scripts/check', 'scripts/verify', 'scripts/check-adoption.py'):
            self.file(name, '#!/usr/bin/env bash\nexit 2\n')
        self.file('scripts/validation.sh',
                  '#!/usr/bin/env bash\npython3 scripts/check-adoption.py\nexit 2\n')

    def file(self, name, text):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding='utf-8')

    def guard(self):
        return subprocess.run([sys.executable, str(GUARD), '--root', str(self.root)],
                              capture_output=True, text=True, timeout=10)

    def test_purpose_built_scaffold_passes_without_product_code(self):
        result = self.guard()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('structure: PASS', result.stdout)

    def test_unfilled_authorities_and_kit_readmes_fail(self):
        self.file('AGENTS.md', '# Agent Instructions\n{{PROJECT_PURPOSE}}\n')
        self.file('README.md', '# Project Template\nThis repository is a template kit, not an app.\n')
        self.file('.pi/README.md', '# Pi resources in this kit\n')
        result = self.guard()
        self.assertEqual(result.returncode, 1)
        for name in ('AGENTS.md', 'README.md', '.pi/README.md'):
            self.assertIn(name, result.stderr)

    def test_kit_only_material_and_bootstrap_role_fail(self):
        self.file('tests/test_template.py', '# kit tests\n')
        self.file('tests/test_adoption.py', '# kit tests\n')
        self.file('.pi/prompts/bootstrap.md', 'Adapt this template kit\n')
        self.file('.pi/agents/bootstrap.md', '# Bootstrap role: set up a project, not its first feature\n')
        self.file('templates/project/README.md', '# {{PROJECT_NAME}}\n')
        result = self.guard()
        self.assertEqual(result.returncode, 1)
        for name in ('tests/test_template.py', 'tests/test_adoption.py',
                     '.pi/prompts/bootstrap.md',
                     '.pi/agents/bootstrap.md', 'templates/project/README.md'):
            self.assertIn(name, result.stderr)

    def test_wholesale_optional_library_fails_but_selected_starter_passes(self):
        names = ('templates/feature/README.md', 'templates/feature/feature-spec.md',
                 'templates/feature/architecture.md', 'templates/feature/review.md')
        for name in names:
            self.file(name, '# optional starter\n')
        self.assertIn('wholesale feature artifacts', self.guard().stderr)
        (self.root / names[-1]).unlink()
        self.assertEqual(self.guard().returncode, 0)

    def test_broken_authority_links_and_prompt_roles_fail(self):
        self.file('README.md', '# Jumping Potato\n\n[Guide](docs/user/start.md)\n')
        self.file('.pi/prompts/design.md', 'Read `.pi/agents/designer.md` first.\n')
        result = self.guard()
        self.assertEqual(result.returncode, 1)
        self.assertIn('broken local link', result.stderr)
        self.assertIn('missing role .pi/agents/designer.md', result.stderr)

    def test_unwired_adoption_phase_fails(self):
        self.file('scripts/validation.sh', '#!/usr/bin/env bash\n# scripts/check-adoption.py\nexit 2\n')
        result = self.guard()
        self.assertEqual(result.returncode, 1)
        self.assertIn('adoption guard not wired', result.stderr)

    def test_missing_required_files_fail(self):
        (self.root / 'AGENTS.md').unlink()
        (self.root / 'scripts/verify').unlink()
        result = self.guard()
        self.assertEqual(result.returncode, 1)
        self.assertIn('AGENTS.md: missing', result.stderr)
        self.assertIn('scripts/verify: missing', result.stderr)

    def test_this_kit_is_not_an_adopted_project(self):
        result = subprocess.run([sys.executable, str(GUARD)],
                                capture_output=True, text=True, timeout=10)
        self.assertEqual(result.returncode, 1)
        self.assertIn('README.md', result.stderr)


if __name__ == '__main__':
    unittest.main(verbosity=2)
