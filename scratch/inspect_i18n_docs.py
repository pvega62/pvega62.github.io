import json
import re
from pathlib import Path

DOC_ROOT = Path(r'c:\Users\vegap\OneDrive\Documents\GitHub\docusaurus')
HTML_ROOT = Path(r'c:\Users\vegap\OneDrive\Documents\GitHub\pvega62.github.io')

LOCALES = ['ar', 'es', 'fr', 'hi', 'ja', 'zh']

# 1. Check all top-level docs/*.md in English
print('=== All top-level docs/*.md in docusaurus/docs ===')
for md in sorted((DOC_ROOT / 'docs').glob('*.md*')):
    txt = md.read_text(encoding='utf-8')
    fm = re.match(r'^---\s*\n(.*?)\n---', txt, re.S)
    meta = {}
    if fm:
        for line in fm.group(1).splitlines():
            if ':' in line:
                k, v = line.split(':', 1)
                meta[k.strip()] = v.strip().strip("'\"")
    print(f'  {md.name}: id={meta.get("id")}, title={meta.get("title")}, sidebar_label={meta.get("sidebar_label")}, pos={meta.get("sidebar_position")}, slug={meta.get("slug")}')

# 2. Check localized labels in docusaurus/i18n/<loc>
CAT_KEYS = [
    'sidebar.tutorialSidebar.category.Automated job search with Sweepy',
    'sidebar.tutorialSidebar.category.Log and LLM observability',
    'sidebar.tutorialSidebar.category.Sui TypeScript SDK, end to end',
    'sidebar.tutorialSidebar.category.Stripe API',
    'sidebar.tutorialSidebar.category.Blüdhaven Pets API',
    'sidebar.tutorialSidebar.category.Commit and PR write-ups',
]
DOC_FILES = [
    'intro.md',
    'sweepy/intro.mdx',
    'artie-case-study.md',
    'Installing-and-Applying-a-Theme-to-Google-Chrome.md',
    'Using-Writage-to-Write-and-Edit-a-GitHub-Wiki-Page-Directly-From-Microsoft-Word.md',
]

print('\n=== Localized Docusaurus labels ===')
for loc in LOCALES:
    print(f'\n--- {loc} ---')
    cur_json = DOC_ROOT / 'i18n' / loc / 'docusaurus-plugin-content-docs' / 'current.json'
    data = json.loads(cur_json.read_text(encoding='utf-8')) if cur_json.exists() else {}
    for k in CAT_KEYS:
        msg = data.get(k, {}).get('message', 'MISSING')
        print(f'  CAT {k.split(".")[-1]:35s} -> {msg}')
    for df in DOC_FILES:
        p = DOC_ROOT / 'i18n' / loc / 'docusaurus-plugin-content-docs' / 'current' / df
        if not p.exists():
            print(f'  DOC {df}: MISSING')
            continue
        txt = p.read_text(encoding='utf-8')
        fm = re.match(r'^---\s*\n(.*?)\n---', txt, re.S)
        meta = {}
        if fm:
            for line in fm.group(1).splitlines():
                if ':' in line:
                    k, v = line.split(':', 1)
                    meta[k.strip()] = v.strip().strip("'\"")
        print(f'  DOC {df:40s} -> title={meta.get("title")!r} | sidebar_label={meta.get("sidebar_label")!r}')
