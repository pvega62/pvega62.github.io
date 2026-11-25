import re
from pathlib import Path

DOC_ROOT = Path(r'c:\Users\vegap\OneDrive\Documents\GitHub\docusaurus')
HTML_ROOT = Path(r'c:\Users\vegap\OneDrive\Documents\GitHub\pvega62.github.io')

for f in ['index.html', 'aboutme.html', 'ar/index.html', 'ar/aboutme.html', 'es/index.html', 'es/aboutme.html']:
    s = (HTML_ROOT / f).read_text(encoding='utf-8')
    m = re.search(r'id="softwareDocsSubmenuMenu"[^>]*>(.*?)</ul>', s, re.S)
    hrefs = re.findall(r'href="([^"]+)"', m.group(1))
    print(f'{f:18s} first={hrefs[0]}')

# Check what hrefs appear in docusaurus/build/docs/intro/index.html (or intro.html)
p = DOC_ROOT / 'build' / 'docs' / 'intro.html'
if not p.exists():
    p = DOC_ROOT / 'build' / 'docs' / 'intro' / 'index.html'
s = p.read_text(encoding='utf-8')
print('\n=== Docusaurus built links containing /software/docs/category/ ===')
for h in sorted(set(re.findall(r'href="(/software/docs/category/[^"]+)"', s))):
    print(' ', h)
