"""Build a local decision gallery and validate the image collection (standard library)."""
from pathlib import Path
import argparse
import html
import json
import re
import struct

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parents[1]
RESEARCH = REPO / 'research/100-ai-income-opportunities'

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--require-complete', action='store_true')
    args = parser.parse_args()
    ideas = json.loads((RESEARCH / 'ideas.json').read_text())
    files = list(ROOT.glob('ch*/*.png'))
    images = {}
    for file in files:
        match = re.match(r'AI-(\d{3})-', file.name)
        if match:
            key = 'AI-' + match.group(1)
            if key in images:
                raise ValueError('Duplicate topic image: ' + key)
            images[key] = file.relative_to(ROOT).as_posix()
    missing = [i['id'] for i in ideas if i['id'] not in images]
    indexes = {n: ROOT / f'ch{n:02}/00-chapter-index.png' for n in range(1, 21)}
    missing_indexes = [n for n, file in indexes.items() if not file.exists()]
    dimensions = {}
    for file in ROOT.rglob('*.png'):
        data = file.read_bytes()
        if data[:8] != b'\x89PNG\r\n\x1a\n':
            raise ValueError('Not a PNG: ' + str(file))
        w, h = struct.unpack('>II', data[16:24])
        if not 1.7 < w / h < 1.85:
            raise ValueError('Unexpected aspect ratio: ' + str(file))
        dimensions[file.relative_to(ROOT).as_posix()] = [w, h]
    report = {'expected_topics': 100, 'topic_images': len(images),
              'chapter_indexes': 20-len(missing_indexes),
              'master_index': (ROOT/'00-master-index.png').exists(),
              'missing_topics': missing, 'missing_chapters': missing_indexes,
              'native_dimensions': dimensions,
              'checks': 'File identity, unique IDs, PNG headers and landscape aspect ratios. Visual review is recorded in chapter manifests.'}
    report['complete'] = not missing and not missing_indexes and report['master_index'] and len(images) == 100
    (ROOT/'verification.json').write_text(json.dumps(report, indent=2)+'\n')
    if args.require_complete and not report['complete']:
        raise SystemExit('Incomplete collection: '+json.dumps(report, default=str))
    groups = {i['group']: i['industry'] for i in ideas}
    chapter_options = ''.join(f'<option value="{n}">{n:02} — {html.escape(title)}</option>' for n,title in groups.items())
    nav = ''.join(f'<li><a href="ch{n:02}/README.md">{n:02}. {html.escape(title)}</a> · <a href="ch{n:02}/00-chapter-index.png">Index image</a></li>' for n,title in groups.items())
    cards = []
    for i in ideas:
        image = images.get(i['id'])
        art = f'<a href="{image}"><img src="{image}" alt="{html.escape(i["title"])}" loading="lazy"></a>' if image else '<p>Image in production</p>'
        cards.append(f'''<article data-group="{i['group']}" data-level="{i['level']}" data-model="{i['model']}">
{art}<div class="copy"><small>{i['id']} · {html.escape(i['industry'])}</small>
<h2>{html.escape(i['title'])}</h2><p><strong>Buyer:</strong> {html.escape(i['buyer'])}</p>
<p>{html.escape(i['deliverable'])}.</p><p><strong>Assess:</strong> {html.escape(i['skills'])}.</p>
<p><strong>Decide with a test:</strong> {html.escape(i['pilot'])}.</p>
<p class="muted">{i['level']} · {i['model']} · ${i['price_usd']:,} price hypothesis · {i['hours_per_unit']} assumed delivery/support hours per unit</p>
<details><summary>Constraints and evidence</summary><p>{html.escape(i['risk'])}.</p><p>{html.escape(i['evidence_confidence'])}.</p><p>Source IDs: {', '.join(i['source_ids'])}. Exact offer and price unvalidated.</p></details>
<p><a href="../../research/100-ai-income-opportunities/100-IDEAS.md#{i['id'].lower()}">Full research card</a></p></div></article>''')
    page = '''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Assess & Decide — AI Income Opportunities</title>
<style>
:root{color-scheme:dark;font:17px/1.6 system-ui,sans-serif;background:#0b1814;color:#faf7ef}*{box-sizing:border-box}body{max-width:1500px;margin:auto;padding:32px}h1{font-size:clamp(2rem,5vw,3.8rem);line-height:1.1}a{color:#f4b544}header{max-width:1100px;margin-bottom:36px}.eyebrow{letter-spacing:.15em;color:#f4b544}img{display:block;width:100%;height:auto;border-radius:12px}.hero{margin:24px 0}label{min-width:0;display:flex;flex-direction:column;gap:6px}input,select{width:100%;min-width:0;max-width:100%;font:inherit;padding:10px;background:#142823;color:white;border:1px solid #668477;border-radius:6px}.filters{display:grid;grid-template-columns:2fr 2fr 1fr 1fr;gap:14px}#cards{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:26px}article{background:#142823;border:1px solid #355046;border-radius:14px;overflow:hidden}article img{border-radius:0}.copy{padding:22px;overflow-wrap:anywhere}.copy h2{line-height:1.2}.muted,small{color:#c5d0ca}details{margin:16px 0}summary{cursor:pointer}nav ul{columns:2;padding-left:24px}[hidden]{display:none!important}@media(max-width:850px){body{padding:18px}.filters,#cards{grid-template-columns:1fr}nav ul{columns:1}}
</style><header><p class="eyebrow">ASSESS → DECIDE → TEST</p><h1>100 AI Income Opportunities</h1><p>Start with work you know, buyers you can reach, and time you can realistically commit. Choose one small paid test.</p><p>These are research-informed hypotheses. Prices are proposed, revenue is gross before costs, and no income is guaranteed.</p><p><a href="../../research/100-ai-income-opportunities/MASTER-INDEX.md">Master decision guide</a> · <a href="../../research/100-ai-income-opportunities/ECONOMICS.md">Economics & capacity</a> · <a href="../../research/100-ai-income-opportunities/SOURCES.md">Sources</a></p></header>
<a href="00-master-index.png"><img class="hero" src="00-master-index.png" alt="Master index of twenty industry chapters"></a>
<nav><details><summary>Chapter indexes</summary><ul>CHAPTER_NAV</ul></details></nav>
<section aria-label="Filter opportunities"><div class="filters"><label>What work do you know?<select id="group"><option value="">All industries</option>CHAPTER_OPTIONS</select></label><label>Search a skill, buyer or idea<input id="query" type="search" placeholder="e.g. writing, bookkeeping, AI-011"></label><label>Technical entry<select id="level"><option value="">All levels</option><option>Beginner</option><option>Intermediate</option><option>Advanced</option></select></label><label>Delivery model<select id="model"><option value="">All models</option><option>download</option><option>project</option><option>retainer</option><option>subscription</option><option>workshop</option></select></label></div><p id="count" aria-live="polite"></p></section>
<main id="cards">CARDS</main><p id="empty" hidden>No matching ideas. Broaden your filters.</p><footer><p>Data Science Masterminds · Agentic Founder · Kunaal Naik & Arpan Saxena</p><p>Research: 7 November 2026. Images are flattened PNGs; prompts and review notes are retained in chapter manifests.</p></footer>
<script>
const cards=[...document.querySelectorAll('article')];const controls=['group','query','level','model'].map(id=>document.getElementById(id));
function filter(){const [group,q,level,model]=controls.map(c=>c.value.trim().toLowerCase());let shown=0;for(const card of cards){const ok=(!group||card.dataset.group===group)&&(!q||card.textContent.toLowerCase().includes(q))&&(!level||card.dataset.level.toLowerCase()===level)&&(!model||card.dataset.model===model);card.hidden=!ok;if(ok)shown++;}document.getElementById('count').textContent=`${shown} of 100 ideas match. Assess fit before choosing.`;document.getElementById('empty').hidden=shown>0;}controls.forEach(c=>c.addEventListener('input',filter));filter();
</script></html>'''
    page=page.replace('CHAPTER_NAV',nav).replace('CHAPTER_OPTIONS',chapter_options).replace('CARDS','\n'.join(cards))
    (ROOT/'gallery.html').write_text(page)
    print(json.dumps({k:v for k,v in report.items() if k!='native_dimensions'},indent=2))

if __name__ == '__main__':
    main()
