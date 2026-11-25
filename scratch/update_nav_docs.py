"""Update the Software/Dev Docs submenu in all 35 HTML pages to match Docusaurus.

Replaces the contents of <ul ... id="softwareDocsSubmenuMenu"> and
<ul ... id="softwareDocsSubmenuMobileMenu"> with the 11 top-level sidebar
items from the Docusaurus site (in sidebar_position order), using each
locale's exact translated title/label from docusaurus/i18n/ and the exact
category slugs from docusaurus/build/.

Preserves each file's URL prefix ('https://pvega62.github.io/software' on
index.html, '/software' on subpages), indentation, and line endings.
"""
import html as htmlmod
import json
import re
from pathlib import Path

DOC_ROOT = Path(r'c:\Users\vegap\OneDrive\Documents\GitHub\docusaurus')
HTML_ROOT = Path(r'c:\Users\vegap\OneDrive\Documents\GitHub\pvega62.github.io')

LOCALES = ['en', 'ar', 'es', 'fr', 'hi', 'ja', 'zh']

# Ordered list of (path_suffix, kind, key_or_relpath)
ITEMS = [
    ('docs/intro', 'doc', 'intro.md'),
    ('docs/category/automated-job-search-with-sweepy', 'cat', 'Automated job search with Sweepy'),
    ('docs/category/log-and-llm-observability', 'cat', 'Log and LLM observability'),
    ('docs/category/sui-typescript-sdk-end-to-end', 'cat', 'Sui TypeScript SDK, end to end'),
    ('docs/category/stripe-api', 'cat', 'Stripe API'),
    ('docs/category/blüdhaven-pets-api', 'cat', 'Blüdhaven Pets API'),
    ('docs/category/commit-and-pr-write-ups', 'cat', 'Commit and PR write-ups'),
    ('docs/artie-case-study', 'doc', 'artie-case-study.md'),
    ('docs/google-chrome-theme-installation', 'doc', 'Installing-and-Applying-a-Theme-to-Google-Chrome.md'),
    ('docs/word-github-wiki-writage', 'doc', 'Using-Writage-to-Write-and-Edit-a-GitHub-Wiki-Page-Directly-From-Microsoft-Word.md'),
]

CAT_DIRS = {
    'Automated job search with Sweepy': 'sweepy',
    'Log and LLM observability': 'data-pipelines',
    'Sui TypeScript SDK, end to end': 'typescript-tutorial',
    'Stripe API': 'stripe-api',
    'Blüdhaven Pets API': 'pets-api',
    'Commit and PR write-ups': 'cm-pr',
}


def read_doc_label(md_path: Path) -> str:
    txt = md_path.read_text(encoding='utf-8')
    fm = re.match(r'^---\s*\n(.*?)\n---', txt, re.S)
    meta = {}
    if fm:
        for line in fm.group(1).splitlines():
            if ':' in line:
                k, v = line.split(':', 1)
                meta[k.strip()] = v.strip().strip("'\"")
    return meta.get('sidebar_label') or meta['title']


def build_labels(loc: str) -> list[tuple[str, str]]:
    if loc == 'en':
        cur_json = {}
        docs_base = DOC_ROOT / 'docs'
    else:
        cur_json = json.loads(
            (DOC_ROOT / 'i18n' / loc / 'docusaurus-plugin-content-docs' / 'current.json')
            .read_text(encoding='utf-8')
        )
        docs_base = DOC_ROOT / 'i18n' / loc / 'docusaurus-plugin-content-docs' / 'current'

    out = []
    for suffix, kind, ref in ITEMS:
        if kind == 'cat':
            if loc == 'en':
                cat_data = json.loads((docs_base / CAT_DIRS[ref] / '_category_.json').read_text(encoding='utf-8'))
                label = cat_data['label']
            else:
                label = cur_json[f'sidebar.tutorialSidebar.category.{ref}']['message']
        else:
            label = read_doc_label(docs_base / ref)
        out.append((suffix, label))
    return out


UL_RE = re.compile(
    r'(<ul\b[^>]*id="softwareDocsSubmenu(?:Mobile)?Menu"[^>]*>)(.*?)(</ul>)',
    re.S,
)

updated_files = 0
updated_menus = 0

for loc in LOCALES:
    labels = build_labels(loc)
    loc_dir = HTML_ROOT if loc == 'en' else HTML_ROOT / loc
    loc_prefix = '' if loc == 'en' else f'{loc}/'
    for page in ['index.html', 'aboutme.html', 'articles.html',
                 'technical-writing-hardware.html', 'uxwriting.html']:
        fp = loc_dir / page
        raw_bytes = fp.read_bytes()
        newline = '\r\n' if b'\r\n' in raw_bytes else '\n'
        text = raw_bytes.decode('utf-8')

        # Preserve full URL prefix on index.html vs root-relative on subpages
        base_url = (f'https://pvega62.github.io/software/{loc_prefix}'
                    if page == 'index.html'
                    else f'/software/{loc_prefix}')

        def repl(m: re.Match) -> str:
            global updated_menus
            updated_menus += 1
            open_tag, body, close_tag = m.group(1), m.group(2), m.group(3)
            # Detect item indentation from first <li> in existing body
            indent_m = re.search(r'\n([ \t]*)<li>', body)
            indent = indent_m.group(1) if indent_m else '                    '
            close_m = re.search(r'\n([ \t]*)$', body)
            close_indent = close_m.group(1) if close_m else indent[:-2]
            lines = [
                f'{indent}<li><a class="dropdown-item" href="{base_url}{suffix}">{htmlmod.escape(label, quote=False)}</a></li>'
                for suffix, label in labels
            ]
            return open_tag + newline + newline.join(lines) + newline + close_indent + close_tag

        new_text, count = UL_RE.subn(repl, text)
        if count != 2:
            raise RuntimeError(f'{fp}: expected 2 submenus, found {count}')
        if new_text != text:
            fp.write_bytes(new_text.encode('utf-8'))
            updated_files += 1

print(f'Updated {updated_files} files ({updated_menus} submenu blocks)')
