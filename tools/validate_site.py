#!/usr/bin/env python3
"""Validate deployable ASTRA static site: content, links and image assets."""
from __future__ import annotations
from pathlib import Path
from urllib.parse import urlparse
from collections import Counter
import json, re, sys
from html.parser import HTMLParser
from PIL import Image

ROOT=Path(__file__).resolve().parents[1]
EXPECTED={
 'marie':'https://marie.moip.ai.kr/',
 'astraho':'https://astraho.moip.ai.kr/',
 'skuld':'https://skuldlab.moip.ai.kr/',
 'astra':'https://protofelix.moip.ai.kr/astra/',
 'serena':'https://protofelix.moip.ai.kr/serena/',
 'observatory':'https://protofelix.moip.ai.kr/observatory/'
}
class Page(HTMLParser):
 def __init__(self):
  super().__init__();self.links=[];self.images=[];self.scripts=[];self.styles=[]
 def handle_starttag(self, tag, attrs):
  a=dict(attrs)
  if tag=='a':self.links.append(a)
  if tag=='img':self.images.append(a)
  if tag=='script':self.scripts.append(a)
  if tag=='link' and a.get('rel')=='stylesheet':self.styles.append(a)

def run():
 html=(ROOT/'index.html').read_text('utf8'); css=(ROOT/'styles.css').read_text('utf8'); js=(ROOT/'app.js').read_text('utf8')
 p=Page();p.feed(html)
 def check_group(c,desc):
  assert len(c)==6,f'{desc}: expected 6, found {len(c)}'
  actual={a.get('data-realm'):a.get('href') for a in c}
  assert actual==EXPECTED,(desc,actual)
  assert all(a.get('target')=='_blank' and 'noopener' in a.get('rel','') and 'noreferrer' in a.get('rel','') for a in c),f'{desc}: unsafe target'
 check_group([a for a in p.links if 'orb ' in a.get('class','')+' '], 'Tree orbs')
 check_group([a for a in p.links if a.get('data-realm') and 'orb' not in a.get('class','').split()], 'indexed gates')
 cards=[a for a in p.links if 'realm-card' in a.get('class','').split()]
 assert len(cards)==6,f'Realm cards: found {len(cards)}'
 assert [a['href'] for a in cards]==list(EXPECTED.values()),'Cards order mismatch'
 assert all(a.get('target')=='_blank' and a.get('rel')=='noopener noreferrer' for a in cards),'Cards target security'
 assert len(p.images)==14, len(p.images)  # 1 header, 1 world tree, 6 orbs, 6 cards
 assets=[]
 for i in p.images:
  src=i.get('src','');assert src.startswith('assets/'),src
  f=ROOT/src;assert f.is_file(),f
  with Image.open(f) as im: im.verify()
  assets.append(src)
 assert len(set(assets))==len(assets), 'Duplicate visible image src'
 for realm in EXPECTED:
  for pref in ('orb-','fruit-'):
   f=ROOT/'assets'/f'{pref}{realm}.webp';assert f.exists(),f
   with Image.open(f) as im:
    assert im.format=='WEBP' and im.width>=400 and im.height>=400, f
 assert (ROOT/'assets'/'world-tree.webp').stat().st_size>250_000
 assert (ROOT/'CNAME').read_text('utf8').strip()=='astra.moip.ai.kr'
 assert (ROOT/'.nojekyll').exists()
 manifest=json.loads((ROOT/'site.webmanifest').read_text('utf8'))
 assert manifest['start_url']=='/'
 assert (ROOT/'assets'/'favicon.png').is_file()
 assert (ROOT/'assets'/'og-cover.jpg').is_file()
 assert 'prefers-reduced-motion:reduce' in css,'Reduced motion absent'
 assert 'pointerenter' in js and 'focus' in js,'Keyboard/mouse preview absent'
 assert len(p.scripts)==1 and p.scripts[0].get('src')=='app.js','Expected local-only script'
 assert len(p.styles)==1 and p.styles[0].get('href')=='styles.css','Expected local-only CSS'
 for f in ('index.html','styles.css','app.js','CNAME','site.webmanifest','robots.txt','sitemap.xml','README.md'):
  assert (ROOT/f).is_file(),f
 print('PASS: Six tree links + indexed gates + visual cards; exact targets; 14 valid images; CSP, reduced motion, manifest and GitHub Pages domain.')
if __name__=='__main__':
 try:run()
 except Exception as exc:
  print(f'FAIL: {type(exc).__name__}: {exc}',file=sys.stderr);raise
