#!/usr/bin/env python3
"""Check Data scoring, provenance, screenshots and generated links."""
from pathlib import Path
import hashlib
import json
import re
import yaml

ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'evaluations/data/2026-09-27'
data=json.loads((BASE/'data.json').read_text())
products=data['products'];weights=data['weights']
assert len(products)==14 and len({p['repo'] for p in products})==14
snapshot=yaml.safe_load((ROOT/'snapshot.yaml').read_text())
catalog={x['repo'] for x in snapshot['entries'] if x['primary_category']=='data'}
assert {p['repo'] for p in products}==catalog
assert sum(weights.values())==100
ranked=sorted(products,key=lambda p:(-sum(p['score_parts'].values()),p['repo']))
inventory=json.loads((BASE/'screenshot-inventory.json').read_text())
assert len(inventory)==297 and sum(x['redacted'] for x in inventory)==2
assert len({(x['repo'],x['file']) for x in inventory})==297
for p in products:
    assert set(p['score_parts'])==set(weights)
    assert all(isinstance(p['score_parts'][k],int) and 0<=p['score_parts'][k]<=v for k,v in weights.items())
    assert len(p['tested_sha'])==40 and re.fullmatch('[0-9a-f]{40}',p['tested_sha'])
    folder=BASE/p['slug']
    shots=json.loads((folder/'screenshots.json').read_text())
    assert len(shots)>=10,(p['repo'],len(shots))
    assert (folder/'images'/p['hero']).is_file()
    assert len({s['sha256'] for s in shots})==len(shots),(p['repo'],'duplicate image')
    for s in shots:
        f=folder/'images'/s['file']
        assert f.is_file() and hashlib.sha256(f.read_bytes()).hexdigest()==s['sha256'],f
    assert (folder/'evidence/probes.json').is_file() or (folder/'evidence/checks.json').is_file()
    assert (folder/'trial-findings.md').is_file()
    assert (folder/'README.md').is_file() and (folder/'screenshots.md').is_file()
for f in BASE.rglob('*.md'):
    contents=f.read_text()
    assert '/Users/' not in contents,f
    for target in re.findall(r'\]\(([^)]+)\)',contents):
        if re.match(r'https?://|#',target):continue
        dest=f.parent/target.split('#')[0]
        assert dest.exists(),(f,target)
for f in BASE.rglob('*.json'):
    assert '/Users/' not in f.read_text(),f
for f in BASE.rglob('*.html'):
    assert '/Users/' not in f.read_text(),f
print('PASS: 14 Data products; 297 unique images; two redactions; scores, provenance and links')
