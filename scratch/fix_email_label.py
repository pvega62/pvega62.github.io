"""Normalize the Contact dropdown label to 'Email' on the six English pages.

Google's word list rejects 'e-mail'. The label sits inside <nav>, which the
project .vale.ini block-ignores, so Vale never reported it. Only the exact
anchor text changes. Bytes in, bytes out, so line endings survive untouched.
"""
from pathlib import Path

PAGES = ['index.html', 'aboutme.html', 'articles.html',
         'technical-writing-hardware.html', 'uxwriting.html', 'search.html']

OLD = b'>e-mail</a>'
NEW = b'>Email</a>'

total = 0
for page in PAGES:
    p = Path(page)
    data = p.read_bytes()
    before_crlf = data.count(b'\r\n')
    n = data.count(OLD)
    if n:
        data = data.replace(OLD, NEW)
        p.write_bytes(data)
        total += n
        check = p.read_bytes()
        after_crlf = check.count(b'\r\n')
        print(f'{page}: {n} label(s) changed | CRLF {before_crlf} -> {after_crlf}')
    else:
        print(f'{page}: no e-mail label found | CRLF {before_crlf}')

print(f'\ntotal labels changed: {total}')
