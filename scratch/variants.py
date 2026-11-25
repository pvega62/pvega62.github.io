import json
import re
from collections import Counter, defaultdict

lines = open('scratch/typo-probe.txt', encoding='utf-8').read().split('\n')
words = []
for l in lines:
    words.extend(re.findall(r"[A-Za-z][A-Za-z'\u2019\-]{2,}", l))
c = Counter(words)

by = defaultdict(set)
for w in c:
    by[w.lower().replace('-', '')].add(w)

print('=== spelling variants of the same term ===')
found = False
for k, v in sorted(by.items()):
    if len(v) > 1:
        found = True
        print('  ', k, '->', ', '.join(f'{x}({c[x]})' for x in sorted(v)))
if not found:
    print('  none')

print()
print('=== hyphenation consistency ===')
TERMS = ['signup', 'sign-up', 'login', 'log-in', 'walkthrough', 'walk-through',
         'setup', 'set-up', 'email', 'e-mail', 'dropoff', 'drop-off',
         'checkout', 'check-out', 'homepage', 'onboarding', 'on-board',
         'usability', 'wireframe', 'wireframe', 'side-by-side', 'end-to-end',
         'in-app', 'real-time', 'realtime', 'backend', 'back-end', 'frontend',
         'front-end', 'ecommerce', 'e-commerce']
PAGES = ['index.html', 'aboutme.html', 'articles.html',
         'technical-writing-hardware.html', 'uxwriting.html', 'search.html']
for t in TERMS:
    total = 0
    where = []
    for f in PAGES:
        s = open(f, encoding='utf-8').read()
        n = len(re.findall(r'(?<![A-Za-z-])' + re.escape(t) + r'(?![A-Za-z-])', s, re.I))
        if n:
            total += n
            where.append(f'{f}={n}')
    if total:
        print(f'  {t:18s} {total:3d}   ' + ', '.join(where))
