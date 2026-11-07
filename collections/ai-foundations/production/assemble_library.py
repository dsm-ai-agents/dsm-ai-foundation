"""Build a local chapter index/gallery and optionally package completed PNGs."""
import argparse
import hashlib
import html
import json
from pathlib import Path
import struct
import zipfile

ROOT = Path(__file__).resolve().parents[1]
LIBRARY = ROOT / 'visuals' / 'chapters'
CURRICULUM = json.loads((ROOT / 'production' / 'curriculum.json').read_text())


def inspect_chapters():
    chapters = []
    problems = []
    hashes = {}
    for chapter in CURRICULUM:
        folder = LIBRARY / f"ch{chapter['chapter']:02}"
        images = []
        expected = [('index', 'Chapter introduction', '00-chapter-index.png')]
        expected += [(c['id'], c['title'], f"{c['id']:03}-*.png") for c in chapter['concepts']]
        for image_id, title, pattern in expected:
            candidates = sorted(folder.glob(pattern))
            if len(candidates) != 1:
                problems.append(f"ch{chapter['chapter']:02}/{image_id}: expected one PNG, found {len(candidates)}")
                images.append({'id': image_id, 'title': title, 'path': None})
                continue
            path = candidates[0]
            data = path.read_bytes()
            if data[:8] != b'\x89PNG\r\n\x1a\n':
                problems.append(f'Invalid PNG signature: {path}')
                continue
            width, height = struct.unpack('>II', data[16:24])
            if abs(width / height - 16 / 9) > 0.02:
                problems.append(f'Unexpected aspect ratio: {path.name} {width}x{height}')
            digest = hashlib.sha256(data).hexdigest()
            if digest in hashes:
                problems.append(f'Duplicate content: {path} and {hashes[digest]}')
            hashes[digest] = str(path)
            images.append({'id': image_id, 'title': title, 'path': path,
                           'width': width, 'height': height, 'sha256': digest})
        chapters.append({**chapter, 'images': images})
    return chapters, problems


def write_plan():
    lines = ['# 100-image curriculum and chapter plan', '',
             'Brand: Data Science Masterminds. Authors: Kunaal Naik & Arpan Saxena.', '',
             'One continuous journey, organized into 12 chapters. Each chapter has a separate introduction/index image in addition to its numbered concept images. Total: 100 concepts + 12 chapter introductions = 112 PNGs. No extra all-concept overview or timed slide.', '',
             'All images in this first complete collection use the approved Agentic Accelerator APEX visual treatment. Program mapping can reuse concepts; it does not add to the concept count.', '']
    for c in CURRICULUM:
        lines += [f"## Chapter {c['chapter']:02}: {c['title']}", '', c['why'], '',
                  '| Image | Topic | Teaching point | Visual direction |',
                  '| --- | --- | --- | --- |']
        for topic in c['concepts']:
            lines.append(f"| {topic['id']:03} | {topic['title']} | {topic['point']} | {topic['visual']} |")
        lines.append('')
    lines += ['## Production and research', '',
              'See [production rules](production-rules.md) for sources, visual requirements, factual qualifications, and output expectations. Individual chapter notes contain teaching qualifications. These are flattened, generated PNGs; native sizes are recorded in manifests. Editable PowerPoint composition is a separate deliverable.', '']
    (ROOT / 'production' / '100-image-plan.md').write_text('\n'.join(lines))


def write_indexes(chapters, problems):
    total = sum(bool(i.get('path')) for c in chapters for i in c['images'])
    lines = ['# Data Science Masterminds — AI Visual Library', '',
             '**Authors:** Kunaal Naik & Arpan Saxena  |  **Visual treatment:** Agentic Accelerator APEX', '',
             f'**Files present:** {total}/112. The collection comprises 100 numbered concept images and 12 chapter-introduction images.', '',
             'Open [the visual gallery](gallery.html) to browse the images. Keep the chapter folders beside this file when copying to your local folder or OneDrive. Within each folder, `00-chapter-index.png` comes first, followed by the numbered concepts.', '',
             'The PNGs contain flattened text and artwork. Insert them as pictures in PowerPoint; this collection does not contain editable slide elements.', '',
             '| Chapter | Why this chapter matters | Concepts |', '| --- | --- | --- |']
    for c in chapters:
        lines.append(f"| [{c['chapter']:02} · {c['title']}](#chapter-{c['chapter']:02}) | {c['why']} | {c['start']:03}–{c['end']:03} |")
    nav=[]
    sections=[]
    for c in chapters:
        number=c['chapter']
        lines += ['', f'<a id="chapter-{number:02}"></a>', '', f"## {number:02}. {c['title']}", '', c['why'], '']
        nav.append(f'<a href="#ch{number:02}">{number:02} · {html.escape(c["title"])}</a>')
        cards=[]
        for i in c['images']:
            label='Chapter introduction' if i['id']=='index' else f"{i['id']:03} · {i['title']}"
            if i.get('path'):
                rel=i['path'].relative_to(LIBRARY).as_posix()
                lines.append(f'- [{label}]({rel})')
                cards.append(f'<article><a href="{rel}"><img loading="lazy" src="{rel}" alt="{html.escape(label)}"></a><h3>{html.escape(label)}</h3></article>')
            else:
                lines.append(f'- {label} — pending generation')
                cards.append(f'<article class="pending"><h3>{html.escape(label)}</h3><p>Pending generation</p></article>')
        note=LIBRARY/f'ch{number:02}'/'README.md'
        if note.exists():
            lines += ['',f'[Chapter teaching and review notes](ch{number:02}/README.md)']
        sections.append(f'<section id="ch{number:02}"><h2>{number:02} · {html.escape(c["title"])}</h2><p>{html.escape(c["why"])}</p><div class="grid">'+''.join(cards)+'</div></section>')
    (LIBRARY/'INDEX.md').write_text('\n'.join(lines)+'\n')
    template='''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>DSM AI Visual Library</title><style>
    :root{color-scheme:dark}*{box-sizing:border-box}body{margin:0;background:#020b18;color:#f7f8fc;font:16px/1.5 Arial,sans-serif}header,main{max-width:1500px;margin:auto;padding:32px}header{border-bottom:1px solid #234}h1{font-size:clamp(28px,4vw,50px);margin:.2em 0}h2{font-size:28px}h3{font-size:16px;font-weight:500;margin:12px 16px}a{color:#5ec4b6;text-decoration:none}a:hover{text-decoration:underline}.eyebrow{color:#f2a541;letter-spacing:.12em}nav{display:flex;flex-wrap:wrap;gap:10px 22px;margin-top:24px}section{padding:14px 0 38px;scroll-margin-top:15px}section>p{color:#bdc9d8;max-width:900px}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,430px),1fr));gap:20px}article{background:#041b36;border-radius:10px;overflow:hidden;border:1px solid #19334d}img{display:block;width:100%;height:auto}article.pending{min-height:180px;padding:20px}.status{color:#bdc9d8}.search{width:100%;max-width:550px;padding:12px;background:#041b36;border:1px solid #5ec4b6;color:white;border-radius:6px;margin-top:16px}footer{padding:30px;text-align:center;color:#bdc9d8}button{cursor:pointer} @media print{nav,.search{display:none}article{break-inside:avoid}.grid{grid-template-columns:1fr 1fr}}
    </style><header><div class="eyebrow">DATA SCIENCE MASTERMINDS</div><h1>AI Visual Library</h1><p>Kunaal Naik &amp; Arpan Saxena · Agentic Accelerator</p><p class="status">COUNT / 112 images · 12 chapters · 100 concepts</p><label for="search">Find a concept</label><br><input id="search" class="search" type="search" placeholder="Search title, concept number, or chapter…"><nav>NAV</nav></header><main>SECTIONS</main><footer>Local image gallery. Keep chapter folders beside this file.</footer><script>const input=document.querySelector('#search');input.addEventListener('input',()=>{const q=input.value.toLowerCase().trim();document.querySelectorAll('section').forEach(s=>{const chapterMatch=s.querySelector('h2').textContent.toLowerCase().includes(q);let visible=0;s.querySelectorAll('article').forEach(a=>{const show=!q||chapterMatch||a.textContent.toLowerCase().includes(q);a.hidden=!show;if(show)visible++});s.hidden=!visible})});</script></html>'''
    (LIBRARY/'gallery.html').write_text(template.replace('COUNT',str(total)).replace('NAV',''.join(nav)).replace('SECTIONS',''.join(sections)))
    record={'expected':112,'present':total,'problems':problems,
            'images':[{**i,'path':str(i['path'].relative_to(LIBRARY))} for c in chapters for i in c['images'] if i.get('path')]}
    (LIBRARY/'verification.json').write_text(json.dumps(record,indent=2)+'\n')
    return total


def package(chapters):
    out=ROOT/'exports'
    out.mkdir(exist_ok=True)
    selected_files=[]
    for chapter in chapters:
        folder=LIBRARY/f"ch{chapter['chapter']:02}"
        chapter_files=[i['path'] for i in chapter['images']]
        for name in ['README.md','manifest.json']:
            path=folder/name
            if not path.exists():
                raise SystemExit(f'Missing chapter documentation: {path}')
            chapter_files.append(path)
        selected_files.extend(chapter_files)
        with zipfile.ZipFile(out/f"DSM-Chapter-{chapter['chapter']:02}.zip",'w',zipfile.ZIP_DEFLATED) as z:
            for f in sorted(chapter_files):
                z.write(f,Path('DSM-AI-Visual-Library')/f.relative_to(LIBRARY))
    selected_files.extend(LIBRARY/name for name in ['INDEX.md','gallery.html','verification.json','START-HERE.txt'])
    archive=out/'DSM-AI-Visual-Library.zip'
    with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED) as z:
        for f in sorted(selected_files):
            z.write(f,Path('DSM-AI-Visual-Library')/f.relative_to(LIBRARY))
        z.write(ROOT/'production'/'100-image-plan.md','DSM-AI-Visual-Library/100-image-plan.md')
        z.write(ROOT/'production'/'production-rules.md','DSM-AI-Visual-Library/production-rules.md')
    with zipfile.ZipFile(archive) as z:
        assert z.testzip() is None
        assert sum(n.endswith('.png') for n in z.namelist())==112
    delivery=['# Package the AI Visual Library','','The committed images are in [visuals/chapters](../visuals/chapters/INDEX.md). ZIP bundles are generated locally and are not tracked in Git.','','From this collection folder, run `python production/assemble_library.py --require-complete --package` using Python 3. This uses the standard library and creates the archives linked below. These links work after local generation; the ZIPs are not hosted in this repository.','','[Complete collection](DSM-AI-Visual-Library.zip): 100 concept PNGs, 12 chapter-index PNGs, a searchable local gallery, a master Markdown index, and chapter teaching notes.','','Extract the full collection into your local or OneDrive folder, then open `DSM-AI-Visual-Library/gallery.html`.','','## Individual chapters','','| Chapter | Download |','| --- | --- |']
    for c in chapters:
        delivery.append(f"| {c['chapter']:02}. {c['title']} | [ZIP](DSM-Chapter-{c['chapter']:02}.zip) |")
    delivery+=['','Images are flattened PNGs at their native generated sizes, approximately 16:9. They are ready to insert into PowerPoint as pictures; editable typography and slide objects are not included.','']
    (out/'README.md').write_text('\n'.join(delivery))
    return archive


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--package',action='store_true')
    parser.add_argument('--require-complete',action='store_true')
    args=parser.parse_args()
    write_plan()
    chapters,problems=inspect_chapters()
    total=write_indexes(chapters,problems)
    print(json.dumps({'present':total,'expected':112,'problems':problems},indent=2))
    if args.require_complete and problems:
        raise SystemExit('Library incomplete or verification failed')
    if args.package:
        if problems:raise SystemExit('Refusing to package incomplete library')
        print(package(chapters))
