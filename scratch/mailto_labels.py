import re

PAGES = ['index.html'] + [d + '/index.html' for d in ['ar', 'es', 'fr', 'hi', 'ja', 'zh']]

print('=== mailto labels by page ===')
for f in PAGES:
    s = open(f, encoding='utf-8').read()
    labels = re.findall(r'mailto:[^"]+"[^>]*>([^<]{0,40})<', s)
    print(f'{f:18s} {sorted(set(labels))}')

print()
print('=== contact dropdown heading text ===')
for f in PAGES:
    s = open(f, encoding='utf-8').read()
    m = re.findall(r'dropdown-toggle[^>]*>\s*([^<]{2,30})', s)
    print(f'{f:18s} {sorted(set(x.strip() for x in m))}')
