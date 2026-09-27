#!/usr/bin/env python3
"""Import one local Data trial into the public evaluation tree.

The original trial directory remains untouched. Pass its root explicitly; no
machine-specific path is stored in the repository.
"""
import argparse
import hashlib
import json
import re
import shutil
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'evaluations/data/2026-09-27'
PRODUCTS=json.loads((BASE/'data.json').read_text())['products']


def clean(value: str) -> str:
    value=re.sub(r'/Users/[^/]+/Applications/TradingTrials/2026-09-27-data/',
                 '[local trial checkout]/',value)
    value=re.sub(r'/Users/[^/]+/Documents/Codex/Workspaces/product-lab-use/',
                 '[local trial workspace]/',value)
    value=re.sub(r'/Users/[^/]+/', '[local home]/', value)
    return value


def image_kind(slug: str, name: str) -> str:
    if slug=='04-watchlist' and name.startswith(('01-','02-','03-','04-','05-','06-','07-','08-')):
        return '原生静态页面'
    if slug in ('10-datafeed','11-trump-code','12-intel','13-quant-data-pipeline'):
        if 'native' in name or slug=='11-trump-code' and 'dashboard-' in name or name=='13-dashboard-section.png':
            return '原生产品界面'
    return 'Product Lab 辅助证据页（非上游原生 UI）'


parser=argparse.ArgumentParser()
parser.add_argument('--trial-root',required=True,type=Path)
args=parser.parse_args()
inventory=[]
for product in PRODUCTS:
    slug=product['slug']
    source=args.trial_root/slug
    if not source.is_dir():raise SystemExit(f'missing {source}')
    target=BASE/slug
    target.mkdir(parents=True,exist_ok=True)
    images=target/'images';images.mkdir(exist_ok=True)
    screenshots=sorted((source/'evidence/screenshots').glob('*.png'))
    if len(screenshots)<10:raise SystemExit(f'{slug}: fewer than ten screenshots')
    gallery=[]
    for f in screenshots:
        override=(source/'evidence/public-screenshots'/f.name)
        # The two re-captured public images use explicit source names.
        if slug=='06-adata' and f.name=='18-adata.png':override=source/'evidence/public-screenshots/18-06-adata.png'
        if slug=='09-a-stock-data' and f.name=='01-a-stock-data.png':override=source/'evidence/public-screenshots/01-09-a-stock-data.png'
        use=override if override.exists() else f
        if slug in ('06-adata','09-a-stock-data') and f.name in ('18-adata.png','01-a-stock-data.png') and use==f:
            raise SystemExit(f'{slug}: missing redacted public image {f.name}')
        dest=images/f.name
        shutil.copyfile(use,dest)
        original_hash=hashlib.sha256(f.read_bytes()).hexdigest()
        public_hash=hashlib.sha256(dest.read_bytes()).hexdigest()
        kind=image_kind(slug,f.name)
        row={'file':f.name,'sha256':public_hash,'kind':kind,'redacted':use!=f}
        gallery.append(row)
        inventory.append({'repo':product['repo'],'slug':slug,'file':f.name,
                          'original_sha256':original_hash,'public_sha256':public_hash,
                          'kind':kind,'redacted':use!=f})
    (target/'screenshots.json').write_text(json.dumps(gallery,ensure_ascii=False,indent=2)+'\n')
    note=clean((source/'findings.md').read_text())
    note=note.replace('(evidence/screenshots/)','(screenshots.md)')
    (target/'trial-findings.md').write_text(note)
    out=target/'evidence';out.mkdir(exist_ok=True)
    for f in (source/'evidence').iterdir():
        if not f.is_file() or f.suffix not in ('.json','.html','.md','.txt'):continue
        if f.name=='public-index.html':continue
        (out/f.name).write_text(clean(f.read_text(errors='replace')))
    # Every public detail page has a representative screenshot.
    if not (images/product['hero']).is_file():raise SystemExit(f'{slug}: hero missing')
(BASE/'screenshot-inventory.json').write_text(json.dumps(inventory,ensure_ascii=False,indent=2)+'\n')
print('Imported',len(PRODUCTS),'products and',len(inventory),'screenshots;',sum(x['redacted'] for x in inventory),'public re-captures')
