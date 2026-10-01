import re

# 1. Update docs-button-ja.svg
with open('images/docs-button-ja.svg', 'r', encoding='utf-8') as f:
    ja_svg = f.read()

ja_svg = re.sub(r'<svg width="\d+" height="38" viewBox="0 0 \d+ 38"', '<svg width="300" height="38" viewBox="0 0 300 38"', ja_svg)
ja_svg = re.sub(r'<rect x="0.5" y="0.5" width="\d+"', '<rect x="0.5" y="0.5" width="299"', ja_svg)
ja_svg = re.sub(r'<text x="[^"]+" y="25" fill="#1F3850" font-family="[^"]+" font-weight="bold" font-size="[^"]+" text-anchor="middle">.*?</text>',
                '<text x="172.0" y="25" fill="#1F3850" font-family="Arial, Helvetica, sans-serif" font-weight="bold" font-size="14" text-anchor="middle">ソフトウェア / 開発ドキュメント</text>', ja_svg)

with open('images/docs-button-ja.svg', 'w', encoding='utf-8') as f:
    f.write(ja_svg)

# 2. Update docs-button-es.svg
with open('images/docs-button-es.svg', 'r', encoding='utf-8') as f:
    es_svg = f.read()

es_svg = re.sub(r'<svg width="\d+" height="38" viewBox="0 0 \d+ 38"', '<svg width="280" height="38" viewBox="0 0 280 38"', es_svg)
es_svg = re.sub(r'<rect x="0.5" y="0.5" width="\d+"', '<rect x="0.5" y="0.5" width="279"', es_svg)
es_svg = re.sub(r'<text x="[^"]+" y="25" fill="#1F3850" font-family="[^"]+" font-weight="bold" font-size="[^"]+" text-anchor="middle">.*?</text>',
                '<text x="162.0" y="25" fill="#1F3850" font-family="Arial, Helvetica, sans-serif" font-weight="bold" font-size="15" text-anchor="middle">Documentación de Software</text>', es_svg)

with open('images/docs-button-es.svg', 'w', encoding='utf-8') as f:
    f.write(es_svg)

# 3. Update docs-button-fr.svg
with open('images/docs-button-fr.svg', 'r', encoding='utf-8') as f:
    fr_svg = f.read()

fr_svg = re.sub(r'<text x="[^"]+" y="25" fill="#1F3850" font-family="[^"]+" font-weight="bold" font-size="[^"]+" text-anchor="middle">.*?</text>',
                '<text x="144.0" y="25" fill="#1F3850" font-family="Arial, Helvetica, sans-serif" font-weight="bold" font-size="14.5" text-anchor="middle">Documentation Logicielle</text>', fr_svg)

with open('images/docs-button-fr.svg', 'w', encoding='utf-8') as f:
    f.write(fr_svg)

# 4. Update ja/index.html
with open('ja/index.html', 'r', encoding='utf-8') as f:
    ja_html = f.read()

ja_html = re.sub(r'<img src="/images/docs-button-ja\.svg" alt="ソフトウェア / 開発ドキュメント" width="\d+" height="38">',
                 '<img src="/images/docs-button-ja.svg" alt="ソフトウェア / 開発ドキュメント" width="300" height="38">', ja_html)

with open('ja/index.html', 'w', encoding='utf-8') as f:
    f.write(ja_html)

# 5. Update es/index.html
with open('es/index.html', 'r', encoding='utf-8') as f:
    es_html = f.read()

es_html = re.sub(r'<img src="/images/docs-button-es\.svg" alt="Documentación de Software" width="\d+" height="38">',
                 '<img src="/images/docs-button-es.svg" alt="Documentación de Software" width="280" height="38">', es_html)

with open('es/index.html', 'w', encoding='utf-8') as f:
    f.write(es_html)

# 6. Update hi/index.html
with open('hi/index.html', 'r', encoding='utf-8') as f:
    hi_html = f.read()

hi_html = re.sub(r'<img alt="[^"]+" height="38" src="/images/docs-button-hi\.svg" width="\d+"[ /]*>',
                 '<img src="/images/docs-button-hi.svg" alt="सॉफ़्टवेयर/डेव दस्तावेज़" width="220" height="38">', hi_html)

with open('hi/index.html', 'w', encoding='utf-8') as f:
    f.write(hi_html)

print('Applied all button and HTML updates successfully!')
