#!/usr/bin/env python3
"""Structural regressions for this distribution (not an end-to-end Pi session).

Run: python3 -m unittest discover -s tests -p 'test_*.py'
"""
from __future__ import annotations

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROMPTS = {
    'bootstrap': 'bootstrap',
    'design': 'designer',
    'scout': 'scout',
    'architecture': 'architect',
    'implement': 'implementer',
    'review': 'reviewer',
    'specialist-review': 'specialist-reviewer',
    'docs': 'technical-writer',
    'handoff': 'handoff',
}


class DistributionTests(unittest.TestCase):
    def test_prompts_and_roles_exist_and_are_connected(self):
        self.assertEqual({p.stem for p in (ROOT / '.pi/prompts').glob('*.md')},
                         set(PROMPTS))
        for command, role in PROMPTS.items():
            with self.subTest(command=command):
                path = ROOT / '.pi/prompts' / f'{command}.md'
                text = path.read_text(encoding='utf-8')
                self.assertTrue(text.startswith('---\n'), path)
                _, frontmatter, body = text.split('---', 2)
                self.assertRegex(frontmatter, r'(?m)^description: .+$')
                self.assertRegex(frontmatter, r'(?m)^argument-hint: .+$')
                self.assertIn(f'.pi/agents/{role}.md', body)
                self.assertTrue((ROOT / '.pi/agents' / f'{role}.md').is_file())

    def test_bootstrap_setup_only_contract(self):
        text = (ROOT / '.pi/agents/bootstrap.md').read_text(encoding='utf-8')
        rows = re.findall(r'^\| (\d+) \| ([^|]+) \|', text, re.M)
        self.assertEqual([int(number) for number, _ in rows], list(range(1, 12)))
        self.assertTrue(all(label.strip() in ('**Required**', 'Optional')
                            or label.strip().startswith('**Conditional:')
                            for _, label in rows))
        self.assertIn('300/500', text)
        self.assertIn('80%/90%', text)
        self.assertIn('**exactly one genuinely blocking setup question per message**', text)
        self.assertIn('not as a form to show the user', text)
        self.assertIn('**Do not write product source', text)
        self.assertIn('first-version gameplay/features', text)
        self.assertIn('current **remote HEAD**', text)
        self.assertIn('operator specifies a **tag**', text)
        self.assertIn('compare that clone to the selected remote ref', text)
        self.assertIn('bootstrap complete; product\nimplementation not started', text)
        prompt = (ROOT / '.pi/prompts/bootstrap.md').read_text(encoding='utf-8')
        readme = (ROOT / 'README.md').read_text(encoding='utf-8')
        self.assertIn('one genuinely blocking **setup** question per message', prompt)
        self.assertIn('Once the foundation is reported, stop', prompt)
        self.assertIn('**It does not implement the application', readme)
        self.assertIn('current remote HEAD', readme)
        self.assertIn('operator may\nspecify a **tag**', readme)

    def test_local_markdown_links_resolve(self):
        for path in ROOT.rglob('*.md'):
            if '.git' in path.parts:
                continue
            for line_number, line in enumerate(path.read_text(encoding='utf-8').splitlines(), 1):
                for target in re.findall(r'(?<!!)\[[^\]]+\]\(([^)]+)\)', line):
                    if target.startswith(('https://', 'http://', '#', 'mailto:')):
                        continue
                    with self.subTest(file=str(path.relative_to(ROOT)), line=line_number):
                        self.assertTrue((path.parent / target.split('#')[0]).exists(), target)

    def test_private_evidence_ignored_and_no_old_guide_references(self):
        ignore = (ROOT / '.gitignore').read_text(encoding='utf-8')
        self.assertIn('.agent-runs/', ignore)
        self.assertIn('.DS_Store', ignore)
        self.assertFalse((ROOT / 'template-guide').exists())
        for path in (ROOT / 'README.md', ROOT / '.pi/README.md',
                     ROOT / 'scripts/validation.sh', ROOT / 'templates/user-docs/README.md'):
            self.assertNotIn('template-guide/', path.read_text(encoding='utf-8'))


if __name__ == '__main__':
    unittest.main(verbosity=2)
