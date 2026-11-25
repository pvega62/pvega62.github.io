"""Verify every sitemap URL resolves to a file in the repo."""

import re
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parent.parent
ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
tree = ET.parse(ROOT / "sitemap.xml")
locs = [e.text.strip() for e in tree.getroot().findall("s:url/s:loc", ns)]

missing, ok = [], 0
for u in locs:
    rel = unquote(u.replace("https://pvega62.github.io/", "")).strip("/")
    if not rel:
        ok += 1
        continue
    cands = [ROOT / rel, ROOT / (rel + ".html"), ROOT / rel / "index.html"]
    if any(c.exists() for c in cands):
        ok += 1
    else:
        missing.append(u)

print(f"sitemap urls: {len(locs)}  resolve: {ok}  missing: {len(missing)}")
for m in missing:
    print("  MISSING:", m)

# Extra check: files not listed in the sitemap
listed = {unquote(u.replace("https://pvega62.github.io/", "")).strip("/") for u in locs}
for p in ("index", "aboutme", "articles", "technical-writing-hardware",
          "uxwriting", "search"):
    if p not in listed and p + ".html" not in listed:
        print("  NOT IN SITEMAP:", p + ".html")
