import json
import re
from pathlib import Path

DOC_ROOT = Path(r'c:\Users\vegap\OneDrive\Documents\GitHub\docusaurus')
HTML_ROOT = Path(r'c:\Users\vegap\OneDrive\Documents\GitHub\pvega62.github.io')

# 1. Check built category slugs in docusaurus/build/docs/category
cats = sorted(p.stem for p in (DOC_ROOT / 'build' / 'docs' / 'category').glob('*.html'))
print('=== Built Docusaurus category slugs ===')
for c in cats:
    print(' ', c)

# 2. Check the top-level docs & category labels in English
print('\n=== Docusaurus English top-level labels/titles ===')
for cat_dir in ['sweepy', 'data-pipelines', 'typescript-tutorial', 'stripe-api', 'pets-api', 'cm-pr']:
    cat_file = DOC_ROOT / 'docs' / cat_dir / '_category_.json'
    data = json.loads(cat_file.read_text(encoding='utf-8'))
    print(f'  {cat_dir}: label={data["label"]!r}')

for doc in ['intro.md', 'sweepy/intro.mdx', 'artie-case-study.md',
            'Installing-and-Applying-a-Theme-to-Google-Chrome.md',
            'Using-Writage-to-Write-and-Edit-a-GitHub-Wiki-Page-Directly-From-Microsoft-Word.md']:
    txt = (DOC_ROOT / 'docs' / doc).read_text(encoding='utf-8')
    fm = re.match(r'^---\s*\n(.*?)\n---', txt, re.S)
    title = sidebar_label = slug = None
    if fm:
        for line in fm.group(1).splitlines():
            if line.startswith('title:'): title = line.split(':', 1)[1].strip().strip("'\"")
            if line.startswith('sidebar_label:'): sidebar_label = line.split(':', 1)[1].strip().strip("'\"")
            if line.startswith('slug:'): slug = line.split(':', 1)[1].strip().strip("'\"")
    print(f'  {doc}: title={title!r}, sidebar_label={sidebar_label!r}, slug={slug!r}')

# 3. Check current navbar links in pvega62.github.io/index.html
idx_html = (HTML_ROOT / 'index.html').read_text(encoding='utf-8')
m = re.search(r'id="softwareDocsSubmenuMenu"[^>]*>(.*?)</ul>', idx_html, re.S)
print('\n=== Current pvega62.github.io/index.html softwareDocsSubmenuMenu ===')
if m:
    for href, label in re.findall(r'href="([^"]+)"[^>]*>([^<]+)</a>', m.group(1)):
        print(f'  {label!r:42s} -> {href}')

# 4. Check all html files in pvega62.github.io for softwareDocsSubmenu
all_html = sorted(HTML_ROOT.glob('*.html')) + sorted(HTML_ROOT.glob('*/*.html'))
with_menu = [p.relative_to(HTML_ROOT).as_posix() for p in all_html if 'softwareDocsSubmenu' in p.read_text(encoding='utf-8')]
print(f'\n=== HTML files with softwareDocsSubmenu ({len(with_menu)}) ===')
print(' ', ', '.join(with_menu))
