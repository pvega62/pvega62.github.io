"""Doubled words that inline tags separate, plus spacing around tags."""
import re

PAGES = ['index.html', 'aboutme.html', 'articles.html',
         'technical-writing-hardware.html', 'uxwriting.html', 'search.html']

for page in PAGES:
    raw = open(page, encoding='utf-8').read()
    raw = re.sub(r'<(script|style|svg|template)\b[^>]*>.*?</\1\s*>', ' ', raw, flags=re.S | re.I)
    for n, line in enumerate(raw.split('\n'), start=1):
        flat = re.sub(r'<[^>]+>', ' ', line)
        flat = re.sub(r'&[a-z]+;', ' ', flat)
        flat = re.sub(r'\s+', ' ', flat)
        for m in re.finditer(r'\b(\w+)\s+\1\b', flat, re.I):
            print(f'{page}:{n}  doubled: {m.group(0)!r}  ...{flat[max(0,m.start()-60):m.end()+60]}...')
