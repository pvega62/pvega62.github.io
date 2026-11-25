import re
from pathlib import Path

DOC_ROOT = Path(r'c:\Users\vegap\OneDrive\Documents\GitHub\docusaurus')
p = DOC_ROOT / 'build' / 'docs' / 'intro.html'
if not p.exists():
    p = DOC_ROOT / 'build' / 'docs' / 'intro' / 'index.html'

s = p.read_text(encoding='utf-8')
m = re.search(r'<aside[^>]*theme-doc-sidebar-container[^>]*>(.*?)</aside>', s, re.S)
if m:
    links = re.findall(r'class="menu__link[^"]*"[^>]*href="([^"]+)"[^>]*>(.*?)</a>', m.group(1), re.S)
    for href, txt in links:
        txt = re.sub(r'<[^>]+>', '', txt).strip()
        print(f'{txt:52s} -> {href}')
else:
    print('aside not found')
