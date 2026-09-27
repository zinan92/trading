#!/usr/bin/env python3
"""Validate scores, evidence, gallery assets and relative Markdown links."""
from pathlib import Path
import json,re,hashlib
ROOT=Path(__file__).resolve().parents[1];BASE=ROOT/'evaluations/full-trading-system/2026-09-26'
d=json.loads((BASE/'data.json').read_text());ps=d['products'];assert len(ps)==14
assert len({p['repo'] for p in ps})==14
for p in ps:
 assert sum(p['score_parts'].values())==p['score']
 assert p['score_parts']['execution_verified']==0
 assert all(0<=v<=d['weights'][k] for k,v in p['score_parts'].items())
 assert p['tested_revision'] and len(p['catalog_lock'])==40
 assert p['screenshots'],p['slug']
 for s in p['screenshots']:
  f=BASE/p['slug']/'images'/s['file'];assert f.is_file(),f
  assert hashlib.sha256(f.read_bytes()).hexdigest()==s['public_sha256']
 assert (BASE/p['slug']/'evidence.json').is_file()
 assert (BASE/p['slug']/'preview.jpg').is_file()
readme=(ROOT/'README.md').read_text()
assert readme.count('<!-- EVALUATION:START -->')==1
assert readme.count('<!-- EVALUATION:END -->')==1
ranked=sorted(ps,key=lambda p:(-p['score'],p['repo']))
positions=[readme.index(f"| {i} | [{p['repo'].split('/')[-1]}]") for i,p in enumerate(ranked,1)]
assert positions==sorted(positions)
files=[ROOT/'README.md']+list(BASE.rglob('*.md'))
for f in files:
 txt=f.read_text()
 assert '/Users/' not in txt,f
 for target in re.findall(r'\]\(([^)]+)\)',txt):
  if re.match(r'https?://|#',target):continue
  target=target.split('#')[0]
  assert (f.parent/target).exists(),(str(f),target)
for f in BASE.rglob('*.json'):
 assert '/Users/' not in f.read_text(),f
inv=json.loads((BASE/'screenshot-inventory.json').read_text())
assert sum(x['status']=='published' for x in inv)==sum(len(p['screenshots']) for p in ps)
assert len(inv)==366
print('PASS: 14 products; scores, versions,',sum(len(p['screenshots']) for p in ps),'images, provenance and Markdown links')
