"""Build a spelling probe from EVERY text source Vale skips on the HTML pages.

Sources captured:
  - text nodes anywhere in the document (including nav, footer, head <title>)
  - alt / title / aria-label / placeholder attribute values
  - <meta content> values (description, og:*, twitter:*)
  - JSON-LD string values

Each string lands on its own line so a Vale line number maps back to a
source line. The map is written to scratch/typo-map.json.
"""
import json
import re
import html as htmlmod
from pathlib import Path

PAGES = [
    'index.html',
    'aboutme.html',
    'articles.html',
    'technical-writing-hardware.html',
    'uxwriting.html',
    'search.html',
]

TAG_RE = re.compile(r'<[^>]*>', re.S)
SKIP_BLOCK = re.compile(r'<(script|style|svg|template)\b[^>]*>.*?</\1\s*>', re.S | re.I)
ATTR_RE = re.compile(
    r'\b(alt|title|aria-label|placeholder|aria-description)\s*=\s*"([^"]*)"', re.I
)
META_RE = re.compile(r'<meta\b[^>]*\bcontent\s*=\s*"([^"]*)"', re.I)
JSONLD_RE = re.compile(r'"(@type|name|description|headline)"\s*:\s*"([^"]*)"', re.I)


def line_of(text, offset):
    return text.count('\n', 0, offset) + 1


def clean(s):
    s = htmlmod.unescape(s)
    s = s.replace('\u2019', "'").replace('\u201c', '"').replace('\u201d', '"')
    s = re.sub(r'\s+', ' ', s).strip()
    return s


def words_only(s):
    """Keep strings that plausibly contain prose worth spelling."""
    return bool(re.search(r'[A-Za-z]{2,}', s))


records = []  # (page, line, kind, text)

for page in PAGES:
    raw = Path(page).read_text(encoding='utf-8', errors='replace')
    stripped = SKIP_BLOCK.sub(lambda m: re.sub(r'[^\n]', ' ', m.group(0)), raw)

    for m in ATTR_RE.finditer(raw):
        val = clean(m.group(2))
        if words_only(val):
            records.append((page, line_of(raw, m.start()), m.group(1), val))

    for m in META_RE.finditer(raw):
        val = clean(m.group(1))
        if words_only(val):
            records.append((page, line_of(raw, m.start()), 'meta', val))

    for m in JSONLD_RE.finditer(raw):
        val = clean(m.group(2))
        if words_only(val):
            records.append((page, line_of(raw, m.start()), 'jsonld', val))

    # Text nodes: split the tag-stripped source on tag boundaries.
    pos = 0
    for m in TAG_RE.finditer(stripped):
        chunk = stripped[pos:m.start()]
        for piece in re.split(r'\n', chunk):
            val = clean(piece)
            if words_only(val):
                records.append((page, line_of(stripped, pos), 'text', val))
        pos = m.end()
    tail = stripped[pos:]
    for piece in re.split(r'\n', tail):
        val = clean(piece)
        if words_only(val):
            records.append((page, line_of(stripped, pos), 'text', val))

# De-duplicate identical strings but keep the first source location.
seen = {}
for rec in records:
    seen.setdefault(rec[3], rec)
records = list(seen.values())

probe_lines = []
mapping = {}
for idx, (page, line, kind, text) in enumerate(records, start=1):
    probe_lines.append(text)
    mapping[str(idx)] = {'page': page, 'line': line, 'kind': kind}

Path('scratch/typo-probe.txt').write_text('\n'.join(probe_lines) + '\n', encoding='utf-8')
Path('scratch/typo-map.json').write_text(json.dumps(mapping, indent=0), encoding='utf-8')
print(f'probe strings: {len(records)}')
print(f'sources: ' + ', '.join(f'{k}={sum(1 for r in records if r[2]==k)}' for k in sorted({r[2] for r in records})))
