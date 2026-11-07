"""Build the collection catalog from project manifests (Python standard library)."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def cell(value):
    return str(value).replace('|', '&#124;').replace('\n', ' ')


def build_catalog(root=ROOT):
    lines = ['# Research collections', '', '[Studio home](../README.md)', '',
             'Phase status reflects saved artifacts, not market validation. Detailed articles and public web pages are tracked separately from research cards and local galleries.', '',
             '| Collection | Program | Topics | Research | Writing | Visuals | Web | Gallery |',
             '| --- | --- | --- | --- | --- | --- | --- | --- |']
    for path in sorted((root / 'collections').glob('*/project.json')):
        project = json.loads(path.read_text())
        slug = path.parent.name
        gallery = project.get('gallery')
        link = f'[Open]({slug}/{gallery})' if gallery else 'Planned'
        phases = project['phases']
        row = [f"[{cell(project['title'])}]({slug}/README.md)", cell(project['program']),
               project['expected_topics'], *(phases[k] for k in ('research', 'written', 'visuals', 'web')), link]
        lines.append('| ' + ' | '.join(map(str, row)) + ' |')
    lines += ['', 'Create a new collection with `python tools/new_research.py <slug> --title "Title" --program "Program"` from the repository root. See the [workflow](../docs/WORKFLOW.md).', '']
    (root / 'collections' / 'README.md').write_text('\n'.join(lines))


if __name__ == '__main__':
    build_catalog()
    print('Updated collections/README.md')
