import re
from pathlib import Path

DOC_BUILD = Path(r'c:\Users\vegap\OneDrive\Documents\GitHub\docusaurus\build')
HTML_ROOT = Path(r'c:\Users\vegap\OneDrive\Documents\GitHub\pvega62.github.io')

UL_RE = re.compile(r'<ul\b[^>]*id="softwareDocsSubmenu(?:Mobile)?Menu"[^>]*>(.*?)</ul>', re.S)

checked = 0
missing = []

for fp in sorted(HTML_ROOT.glob('*.html')) + sorted(HTML_ROOT.glob('*/*.html')):
    s = fp.read_text(encoding='utf-8')
    for m in UL_RE.finditer(s):
        for href in re.findall(r'href="([^"]+)"', m.group(1)):
            checked += 1
            rel = re.sub(r'^https://pvega62\.github\.io/software/', '', href)
            rel = re.sub(r'^/software/', '', rel)
            target = DOC_BUILD / (rel + '.html')
            if not target.exists():
                missing.append((fp.relative_to(HTML_ROOT).as_posix(), href, str(target)))

print(f'Checked {checked} submenu links across 35 files; missing in Docusaurus build: {len(missing)}')
for item in missing[:10]:
    print('  MISSING:', item)
