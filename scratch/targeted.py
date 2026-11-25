import re

PAGES = ['index.html', 'aboutme.html', 'articles.html',
         'technical-writing-hardware.html', 'uxwriting.html', 'search.html']

CHECKS = [
    ('lowercase github', r'github'),
    ('ADA casing', r'ADA-[Cc]ompliant'),
    ('docs-as-code casing', r'[Dd]ocs-[Aa]s-[Cc]ode'),
    ('e-mail', r'e-mail'),
    ('Pedro casing', r'[Pp]edro\s+[Vv]ega'),
    ('double space in markup text', r'>[^<]*[A-Za-z]  +[A-Za-z][^<]*<'),
]

for label, pat in CHECKS:
    print(f'=== {label} ===')
    hits = 0
    for f in PAGES:
        lines = open(f, encoding='utf-8').read().split('\n')
        for n, line in enumerate(lines, 1):
            for m in re.finditer(pat, line):
                hits += 1
                start = max(0, m.start() - 70)
                ctx = re.sub(r'\s+', ' ', line[start:m.end() + 70])
                print(f'  {f}:{n}  ...{ctx}...')
    if not hits:
        print('  none')
    print()
