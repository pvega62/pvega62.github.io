"""Spell-check user-facing strings in JS files and inline scripts.

search.html reported zero findings because its copy lives in JavaScript.
Also pulls prose out of README.md.
"""
import json
import re
from pathlib import Path

STR_RE = re.compile(r"""(?<![\w$])(['"`])((?:\\.|(?!\1)[^\\\n]){4,})\1""")
SKIP = re.compile(r'^(https?://|/|\.|#|[a-z-]+\.[a-z]{2,4}$|[A-Za-z0-9_\-]+$|[\d\s.,%:]+$)')

sources = []
for js in Path('.').glob('js/*.js'):
    sources.append((js.name, js.read_text(encoding='utf-8', errors='replace')))
for css in Path('.').glob('css/*.css'):
    pass

for page in ['index.html', 'aboutme.html', 'articles.html',
             'technical-writing-hardware.html', 'uxwriting.html', 'search.html']:
    raw = Path(page).read_text(encoding='utf-8', errors='replace')
    for m in re.finditer(r'<script\b(?![^>]*\bsrc=)[^>]*>(.*?)</script>', raw, re.S | re.I):
        sources.append((f'{page} inline script', m.group(1)))

probe = []
mapping = {}
for name, code in sources:
    for m in STR_RE.finditer(code):
        s = m.group(2)
        if SKIP.match(s.strip()) or ' ' not in s:
            continue
        if not re.search(r'[A-Za-z]{3,}\s+[A-Za-z]{2,}', s):
            continue
        line = code.count('\n', 0, m.start()) + 1
        probe.append(s.replace('\n', ' '))
        mapping[str(len(probe))] = {'file': name, 'line': line}

readme = Path('README.md').read_text(encoding='utf-8', errors='replace')
for n, line in enumerate(readme.split('\n'), start=1):
    clean = re.sub(r'[`*_#>\[\]()|]', ' ', line).strip()
    clean = re.sub(r'https?://\S+', ' ', clean)
    if re.search(r'[A-Za-z]{3,}\s+[A-Za-z]{2,}', clean):
        probe.append(clean)
        mapping[str(len(probe))] = {'file': 'README.md', 'line': n}

Path('scratch/js-probe.md').write_text('\n'.join(probe) + '\n', encoding='utf-8')
Path('scratch/js-map.json').write_text(json.dumps(mapping, indent=0), encoding='utf-8')
print(f'strings: {len(probe)}')
print('files: ' + ', '.join(sorted({m["file"] for m in mapping.values()})))
