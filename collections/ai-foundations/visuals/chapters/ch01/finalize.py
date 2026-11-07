import json, struct
from pathlib import Path
# Historical chapter assembly helper; run only when rebuilding these records.
root=Path(__file__).resolve().parents[3]
curr=json.loads((root/'production/curriculum.json').read_text())
notes={
1:'AI is a broad category; the three capabilities illustrate common tasks rather than an exhaustive definition.',
2:'The fruit example illustrates pattern learning. Machine learning still requires algorithms, objectives, and human design choices.',
3:'Generated content is not guaranteed original, accurate, or suitable for every use; review results.',
4:'Engine/car is an analogy. An application can use several models and external services.',
5:'Prediction and generation are contrasted by task. Generative models can themselves use next-token prediction.',
6:'Supported input/output modes vary by model and application. The diagram is conceptual, not a product capability claim.',
7:'Unsupported does not necessarily mean false; verification needs evidence appropriate to the claim.',
8:'Driving is an analogy for allocating responsibility; no autonomous-driving capability is implied.',
9:'Unstructured content can contain internal structure and structured metadata. The spreadsheet values are illustrative.',
10:'Good inputs improve the basis for a result but do not guarantee correctness. The recipe is an analogy, not a tested cooking instruction.',
11:'These features are illustrative and are not sufficient to uniquely identify all fruit. Labels can also contain errors.',
12:'Sampling bias concerns how a sample is selected and represented, not simply whether it is small.',
13:'Consent is not the only possible lawful basis. Appropriate use also depends on purpose, contracts, law, and organizational policy.',
14:'The forecast is illustrative. It supplies no numerical probability or real weather prediction.',
15:'The example illustrates a possible shared cause. Correlation alone cannot establish the causal mechanism.',
16:'The data are hypothetical. Both table and chart show Monday 2, Tuesday 4, Wednesday 3; Tuesday is highest.'}
for chapter in curr[:2]:
 d=root/'visuals/chapters'/f"ch{chapter['chapter']:02d}"
 jobs=json.loads((d/'jobs.json').read_text())
 images=[]
 for j in jobs:
  f=d/j['filename']
  assert f.exists(),f
  w,h=struct.unpack('>II',f.read_bytes()[16:24])
  images.append(dict(id=j['id'],filename=j['filename'],headline=j['headline'],prompt=j['prompt'],width=w,height=h,review_notes='Visually reviewed: spelling, branding, layout, and concept accuracy. '+ ('All eight topic IDs and names are present.' if j['id']=='index' else notes[j['id']])))
 if chapter['chapter']==1:
  f=d/'004-model-versus-application.png';w,h=struct.unpack('>II',f.read_bytes()[16:24])
  images.append(dict(id=4,filename=f.name,headline='The model is the engine.',reused_from='../../pilot/004-model-vs-application.png',width=w,height=h,review_notes='Reused approved pilot unchanged. '+notes[4]))
 images.sort(key=lambda x:-1 if x['id']=='index' else x['id'])
 if chapter['chapter']==1:
  revision=json.loads((d/'revision-006.json').read_text())
  for im in images:
   if im['id']==6:
    im['original_prompt']=im['prompt']
    im['revision_steps']=[dict(prompt=revision['prompt'],referenced_image=revision['referenced_image']),dict(prompt=revision['final_prompt'],referenced_image=revision['final_reference'])]
    im['prompt']=revision['final_prompt']
    im['referenced_image']=revision['referenced_image']
    im['review_notes']+=' Revised to remove extraneous copy and clutter.'
 manifest=dict(chapter=chapter['chapter'],title=chapter['title'],why=chapter['why'],images=images)
 (d/'manifest.json').write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+'\n')
 lines=[f"# Chapter {chapter['chapter']:02d}: {chapter['title']}",'',chapter['why'],'','Data Science Masterminds · Agentic Accelerator · Kunaal Naik & Arpan Saxena','','## Image index','','| ID | Image |','| --- | --- |']
 for im in images:lines.append(f"| {im['id'] if im['id']=='index' else str(im['id']).zfill(3)} | [{im['headline']}]({im['filename']}) |")
 lines+=['','## Teaching qualifications','']
 for c in chapter['concepts']:lines.append(f"- **{c['id']:03d} — {c['title']}:** {notes[c['id']]}")
 lines+=['','## Sources','','- [Microsoft: Machine Learning for Beginners](https://github.com/microsoft/ML-For-Beginners)','- [Microsoft: Data Science for Beginners](https://github.com/microsoft/Data-Science-For-Beginners)','- [Microsoft: Generative AI for Beginners](https://github.com/microsoft/generative-ai-for-beginners)','','## Review and format','','All images have been visually reviewed for wording, author spelling, readability, concept distinctions, and index completeness. These are flattened PNGs at native generation dimensions, approximately 16:9, not editable PowerPoint slides. Exact sizes and prompts are recorded in manifest.json. Live learner comprehension and projector readability have not yet been tested.']
 (d/'README.md').write_text('\n'.join(lines)+'\n')
 print(d,len(images),'images')
