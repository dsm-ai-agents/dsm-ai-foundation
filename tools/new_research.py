"""Create a research collection without overwriting existing work."""
import argparse
import json
from pathlib import Path
import re
import shutil

from build_catalog import ROOT, build_catalog

PROGRAMS = ('AI Agent Master Class', 'Agentic Accelerator', 'Agentic Founder', 'Unassigned')


def create_collection(root, slug, title, program):
    if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', slug):
        raise ValueError('Use a lowercase slug with letters, numbers, and single hyphens.')
    if not title.strip() or any(c in title for c in '\r\n'):
        raise ValueError('Provide a nonempty, single-line title.')
    if program not in PROGRAMS:
        raise ValueError('Unknown program.')
    destination = root / 'collections' / slug
    if destination.exists():
        raise ValueError(f'Collection already exists: {slug}')
    shutil.copytree(root / 'templates' / 'research-project', destination)
    for path in destination.rglob('*.md'):
        content = path.read_text()
        for token, value in [('{{TITLE}}', title), ('{{SLUG}}', slug), ('{{PROGRAM}}', program)]:
            content = content.replace(token, value)
        path.write_text(content)
    path = destination / 'project.json'
    project = json.loads(path.read_text())
    project.update(slug=slug, title=title, program=program)
    path.write_text(json.dumps(project, indent=2, ensure_ascii=False) + '\n')
    build_catalog(root)
    return destination


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('slug')
    parser.add_argument('--title', required=True)
    parser.add_argument('--program', choices=PROGRAMS, default='Unassigned')
    args = parser.parse_args()
    try:
        result = create_collection(ROOT, args.slug, args.title, args.program)
    except ValueError as error:
        parser.error(str(error))
    print(f'Created {result.relative_to(ROOT)}; fill in the research brief before production.')
