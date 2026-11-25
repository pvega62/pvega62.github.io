import re

LOCALES = ['ar', 'es', 'fr', 'hi', 'ja', 'zh']

print('=== iframe title for spec-incorrect-email.pdf ===')
for d in LOCALES:
    f = f'{d}/uxwriting.html'
    s = open(f, encoding='utf-8').read()
    m = re.search(r'spec-incorrect-email\.pdf"\s+title="([^"]*)"', s)
    h2 = re.search(r'spec-incorrect-email\.pdf.{0,700}?<h2[^>]*>(.*?)</h2>', s, re.S)
    print(f'{f:20s} iframe title: {m.group(1) if m else "none"}')
    print(f'{"":20s} card h2     : {re.sub(r"<[^>]+>", "", h2.group(1)).strip() if h2 else "none"}')

print()
print('=== English parity ===')
s = open('uxwriting.html', encoding='utf-8').read()
m = re.search(r'spec-incorrect-email\.pdf"\s+title="([^"]*)"', s)
h2 = re.search(r'spec-incorrect-email\.pdf.{0,700}?<h2[^>]*>(.*?)</h2>', s, re.S)
print('uxwriting.html       iframe title:', m.group(1))
print('                     card h2     :', re.sub(r'<[^>]+>', '', h2.group(1)).strip())
