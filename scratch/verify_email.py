import re
import glob

HYPH = re.compile(r'e-mail', re.I)
LOWER = re.compile(r'(?<![-\w])email(?![-\w])')
UPPER = re.compile(r'(?<![-\w])Email(?![-\w])')

print('=== remaining hyphenated forms, whole site ===')
found = False
for f in (sorted(glob.glob('*.html')) + sorted(glob.glob('*/*.html'))
          + sorted(glob.glob('js/*.js')) + ['README.md']):
    s = open(f, encoding='utf-8').read()
    hits = [m.group(0) for m in HYPH.finditer(s)]
    if hits:
        found = True
        print(f'  {f}: {hits}')
if not found:
    print('  none')

print()
print('=== English page counts ===')
for f in ['index.html', 'aboutme.html', 'articles.html',
          'technical-writing-hardware.html', 'uxwriting.html', 'search.html']:
    s = open(f, encoding='utf-8').read()
    print(f'  {f:32s} email={len(LOWER.findall(s)):2d}  Email={len(UPPER.findall(s)):2d}')
