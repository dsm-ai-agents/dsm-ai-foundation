"""Validate collection manifests, topic/image counts, and local documentation links."""
from html.parser import HTMLParser
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
STAGES = ('research', 'content', 'production', 'visuals', 'web', 'exports')


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        self.links += [v for k, v in attrs if k in ('href', 'src') and v]


def validate(root=ROOT):
    errors = []
    manifests = sorted((root / 'collections').glob('*/project.json'))
    for manifest in manifests:
        base = manifest.parent
        try:
            p = json.loads(manifest.read_text())
            if p['schema_version'] != 1 or p['slug'] != base.name:
                raise ValueError('invalid schema version or slug')
            for name in STAGES:
                if not (base / name).is_dir():
                    raise ValueError(f'missing stage folder: {name}')
            if not (base / 'README.md').is_file():
                raise ValueError('missing collection README')
            for name in ('research', 'written', 'visuals', 'web'):
                if p['phases'][name] not in ('planned', 'in-progress', 'complete'):
                    raise ValueError(f'invalid phase: {name}')
            for key in ('topic_catalog', 'visuals_path', 'gallery'):
                if p.get(key):
                    target = (base / p[key]).resolve()
                    if not target.is_relative_to(base.resolve()) or not target.exists():
                        raise ValueError(f'invalid or missing {key}: {p[key]}')
            topics = json.loads((base / p['topic_catalog']).read_text())
            if p['topic_format'] == 'chapters':
                topics = [topic for chapter in topics for topic in chapter['concepts']]
            elif p['topic_format'] != 'topics':
                raise ValueError('unknown topic format')
            ids = [topic['id'] for topic in topics]
            if len(ids) != len(set(ids)) or len(ids) != p['expected_topics']:
                raise ValueError('topic count mismatch or duplicate IDs')
            images = list((base / p['visuals_path']).rglob('*.png'))
            if len(images) != p['expected_images']:
                raise ValueError(f'image count: {len(images)} != {p["expected_images"]}')
        except (ValueError, KeyError, TypeError, OSError) as exc:
            errors.append(f'{manifest.relative_to(root)}: {exc}')

    paths = [root / 'README.md']
    for folder in ('collections', 'docs'):
        paths += [p for p in (root / folder).rglob('*') if p.suffix in ('.md', '.html')]
    for path in paths:
        content = path.read_text()
        if path.suffix == '.html':
            parser = Links()
            parser.feed(content)
            links = parser.links
        else:
            content = re.sub(r'```.*?```', '', content, flags=re.S)
            links = re.findall(r'\[[^\]]*\]\(([^\s)]+)(?:\s+"[^"]*")?\)', content)
        for link in links:
            url = urlsplit(link.strip('<>'))
            if url.scheme or url.netloc or not url.path:
                continue
            target = path.parent / unquote(url.path)
            # ZIPs are generated locally and intentionally absent from clean clones.
            if target.suffix == '.zip' and 'exports' in target.parts:
                continue
            if not target.exists():
                errors.append(f'{path.relative_to(root)}: broken link {link}')
    return errors


if __name__ == '__main__':
    problems = validate()
    if problems:
        print('\n'.join(problems))
        raise SystemExit(1)
    print('Collection manifests, topic/image counts, and local file links passed.')
