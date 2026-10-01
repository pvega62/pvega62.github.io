import re

SUPPORTED_LOCALES = ['es', 'fr', 'ar', 'zh', 'ja', 'hi']

def get_localized_portfolio_url(url, locale):
    if not url or not isinstance(url, str):
        return url

    if (
        url.startswith('mailto:') or
        url.startswith('#') or
        'linkedin.com' in url or
        'github.com' in url or
        '/Recordkeeping' in url or
        '/software/' in url or
        url.startswith('/docs') or
        url.startswith('/blog')
    ):
        return url

    is_absolute_portfolio = bool(re.match(r'^https?://pvega62\.github\.io', url, re.IGNORECASE))
    is_relative = url.startswith('/') and not url.startswith('/software')

    if not is_absolute_portfolio and not is_relative:
        return url

    active_locale = locale if locale in SUPPORTED_LOCALES else ''
    lang_prefix = f'/{active_locale}/' if active_locale else '/'

    path = re.sub(r'^https?://pvega62\.github\.io', '', url, flags=re.IGNORECASE) if is_absolute_portfolio else url
    if not path:
        path = '/'

    for loc in SUPPORTED_LOCALES:
        if path == f'/{loc}' or path == f'/{loc}/':
            path = '/'
            break
        if path.startswith(f'/{loc}/'):
            path = path[len(loc) + 1:]
            break

    final_relative_path = lang_prefix
    if path != '/' and path != '':
        clean_subpath = re.sub(r'^\/', '', path)
        clean_subpath = re.sub(r'\.html$', '', clean_subpath)
        if clean_subpath and clean_subpath != 'index':
            final_relative_path = f'{lang_prefix}{clean_subpath}'.replace('//', '/')

    if is_absolute_portfolio:
        return f'https://pvega62.github.io{final_relative_path}'

    return final_relative_path

test_cases = [
    # (url, locale, expected)
    ('https://pvega62.github.io/', 'es', 'https://pvega62.github.io/es/'),
    ('https://pvega62.github.io/', 'en', 'https://pvega62.github.io/'),
    ('https://pvega62.github.io/', 'fr', 'https://pvega62.github.io/fr/'),
    ('https://pvega62.github.io/', 'ar', 'https://pvega62.github.io/ar/'),
    ('https://pvega62.github.io/', 'zh', 'https://pvega62.github.io/zh/'),
    ('https://pvega62.github.io/', 'ja', 'https://pvega62.github.io/ja/'),
    ('https://pvega62.github.io/', 'hi', 'https://pvega62.github.io/hi/'),
    ('https://pvega62.github.io/uxwriting', 'es', 'https://pvega62.github.io/es/uxwriting'),
    ('https://pvega62.github.io/uxwriting', 'en', 'https://pvega62.github.io/uxwriting'),
    ('https://pvega62.github.io/uxwriting', 'zh', 'https://pvega62.github.io/zh/uxwriting'),
    ('https://pvega62.github.io/aboutme', 'es', 'https://pvega62.github.io/es/aboutme'),
    ('https://pvega62.github.io/articles', 'es', 'https://pvega62.github.io/es/articles'),
    ('https://pvega62.github.io/technical-writing-hardware', 'es', 'https://pvega62.github.io/es/technical-writing-hardware'),
    ('/', 'es', '/es/'),
    ('/uxwriting', 'es', '/es/uxwriting'),
    ('/aboutme', 'es', '/es/aboutme'),
    ('https://pvega62.github.io/Recordkeeping/', 'es', 'https://pvega62.github.io/Recordkeeping/'),
    ('https://github.com/pvega62', 'es', 'https://github.com/pvega62'),
    ('https://www.linkedin.com/in/pvega62/', 'es', 'https://www.linkedin.com/in/pvega62/'),
    ('/software/es/docs/intro', 'es', '/software/es/docs/intro'),
    ('/docs/intro', 'es', '/docs/intro'),
    ('/blog', 'es', '/blog'),
]

all_passed = True
for url, locale, expected in test_cases:
    actual = get_localized_portfolio_url(url, locale)
    if actual != expected:
        print(f"FAIL: url={url}, loc={locale} -> got '{actual}', expected '{expected}'")
        all_passed = False
    else:
        print(f"OK: ({url}, {locale}) -> {actual}")

if all_passed:
    print("\nALL URL LOCALIZATION TESTS PASSED!")
