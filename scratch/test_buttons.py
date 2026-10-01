import pymupdf
import re

with open('images/docs-button-ja.svg', 'r', encoding='utf-8') as f:
    ja_svg_base = f.read()

def generate_svg(base_svg, width, font_size, text_x, new_text=None):
    rect_w = width - 1
    svg = base_svg
    svg = re.sub(r'<svg width="\d+" height="38" viewBox="0 0 \d+ 38"', f'<svg width="{width}" height="38" viewBox="0 0 {width} 38"', svg)
    svg = re.sub(r'<rect x="0.5" y="0.5" width="\d+"', f'<rect x="0.5" y="0.5" width="{rect_w}"', svg)
    if new_text:
        svg = re.sub(r'<text x="[^"]+" y="25" fill="#1F3850" font-family="[^"]+" font-weight="bold" font-size="[^"]+" text-anchor="middle">.*?</text>',
                     f'<text x="{text_x}" y="25" fill="#1F3850" font-family="Arial, Helvetica, sans-serif" font-weight="bold" font-size="{font_size}" text-anchor="middle">{new_text}</text>', svg)
    else:
        svg = re.sub(r'<text x="[^"]+" y="25" fill="#1F3850" font-family="[^"]+" font-weight="bold" font-size="[^"]+" text-anchor="middle">(.*?)</text>',
                     f'<text x="{text_x}" y="25" fill="#1F3850" font-family="Arial, Helvetica, sans-serif" font-weight="bold" font-size="{font_size}" text-anchor="middle">\\1</text>', svg)
    return svg

# JA variations
ja_opts = [
    ('ja_w280_fs13', 280, 13, 162),
    ('ja_w280_fs13_5', 280, 13.5, 162),
    ('ja_w290_fs13_5', 290, 13.5, 167),
    ('ja_w290_fs14', 290, 14, 167),
    ('ja_w300_fs14', 300, 14, 172),
]

for name, w, fs, tx in ja_opts:
    svg_code = generate_svg(ja_svg_base, w, fs, tx)
    doc = pymupdf.open(stream=svg_code.encode('utf-8'), filetype='svg')
    pix = doc[0].get_pixmap(dpi=150)
    pix.save(f'C:/Users/vegap/.gemini/antigravity-ide/brain/0f6b9f94-eab0-408f-ac45-8e4fb10979d3/{name}.png')

# ES variations
es_opts = [
    ('es_w270_fs14_5', 270, 14.5, 158, 'Documentación de Software'),
    ('es_w275_fs14_5', 275, 14.5, 160, 'Documentación de Software'),
    ('es_w280_fs14_5', 280, 14.5, 162, 'Documentación de Software'),
    ('es_w280_fs15', 280, 15, 162, 'Documentación de Software'),
    ('es_w265_fs14', 265, 14, 156.5, 'Documentación de Software'),
]

for name, w, fs, tx, txt in es_opts:
    svg_code = generate_svg(ja_svg_base, w, fs, tx, txt)
    doc = pymupdf.open(stream=svg_code.encode('utf-8'), filetype='svg')
    pix = doc[0].get_pixmap(dpi=150)
    pix.save(f'C:/Users/vegap/.gemini/antigravity-ide/brain/0f6b9f94-eab0-408f-ac45-8e4fb10979d3/{name}.png')

# Also check FR with font 14.5
fr_svg = generate_svg(ja_svg_base, 240, 14.5, 144, 'Documentation Logicielle')
doc = pymupdf.open(stream=fr_svg.encode('utf-8'), filetype='svg')
pix = doc[0].get_pixmap(dpi=150)
pix.save('C:/Users/vegap/.gemini/antigravity-ide/brain/0f6b9f94-eab0-408f-ac45-8e4fb10979d3/fr_w240_fs14_5.png')

print('All variations generated successfully!')
