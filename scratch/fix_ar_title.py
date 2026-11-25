"""Replace the one untranslated English title on the Arabic UX page.

The other five locales translate the iframe title and keep only the case-study
prefix localized. Arabic kept the English string verbatim while its card
heading is Arabic, so screen readers announce English on an Arabic page.

The replacement mirrors the sibling locales: localized prefix plus the existing
Arabic card heading, which already names the email error correctly.
"""
from pathlib import Path

p = Path('ar/uxwriting.html')
data = p.read_bytes()
crlf_before = data.count(b'\r\n')

OLD = b'UX Writing Case Study: Incorrect Email Error Message'
# "UX writing case study: an error message about an incorrect email address"
NEW = ('دراسة حالة في كتابة تجربة المستخدم: '
       'رسالة خطأ تتعلق بعنوان بريد إلكتروني غير صحيح').encode('utf-8')

n = data.count(OLD)
print(f'occurrences: {n}')
if n == 1:
    p.write_bytes(data.replace(OLD, NEW))
    check = p.read_bytes()
    print(f'CRLF {crlf_before} -> {check.count(b"\\r\\n")}')
    print(f'bytes {len(data)} -> {len(check)}')
    print('remaining English title:', check.count(OLD))
