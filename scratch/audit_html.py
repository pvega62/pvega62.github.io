"""Structural audit of the English HTML portfolio pages.

Checks document metadata, heading outline, ids, internal and external links,
image alt text, and sitemap coverage. Localized folders are excluded.
"""

import json
import re
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent
PAGES = ["index.html", "aboutme.html", "articles.html",
         "technical-writing-hardware.html", "uxwriting.html", "search.html"]
LOCALES = {"ar", "es", "fr", "hi", "ja", "zh"}


class Collector(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids = []
        self.headings = []
        self.links = []
        self.images = []
        self.metas = {}
        self.title = ""
        self._in_title = False
        self._in_heading = None
        self._heading_buf = []
        self.scripts = 0
        self.styles = 0
        self.svg_count = 0
        self.buttons = 0
        self.iframes = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "script":
            self.scripts += 1
        if tag == "style":
            self.styles += 1
        if tag == "title":
            self._in_title = True
        if tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            self._in_heading = int(tag[1])
            self._heading_buf = []
        if "id" in a:
            self.ids.append(a["id"])
        if tag == "a":
            self.links.append({"href": a.get("href", ""),
                               "aria": a.get("aria-label", ""),
                               "target": a.get("target", "")})
        if tag == "img":
            self.images.append({"src": a.get("src", ""), "alt": a.get("alt"),
                                "loading": a.get("loading")})
        if tag == "meta":
            key = a.get("name") or a.get("property")
            if key:
                self.metas[key] = a.get("content", "")
        if tag == "svg":
            self.svg_count += 1
        if tag == "button":
            self.buttons += 1
        if tag == "iframe":
            self.iframes.append({"src": a.get("src", ""), "title": a.get("title")})

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False
        if tag in ("h1", "h2", "h3", "h4", "h5", "h6") and self._in_heading:
            text = re.sub(r"\s+", " ", "".join(self._heading_buf)).strip()
            self.headings.append({"level": self._in_heading, "text": text})
            self._in_heading = None

    def handle_data(self, data):
        if self._in_title:
            self.title += data
        if self._in_heading:
            self._heading_buf.append(data)


def target_exists(page, href):
    if not href or href.startswith(("#", "mailto:", "tel:", "javascript:", "data:")):
        return None
    p = urlparse(href)
    if p.scheme in ("http", "https"):
        return "external"
    path = p.path
    if not path:
        return "self"
    path = path.lstrip("/")
    top = path.split("/")[0]
    base = ROOT if top in ("images", "css", "js", "styles", "fonts", "samples") else page.parent
    cand = [ROOT / path, base / path]
    if "." not in Path(path).name:
        cand += [ROOT / (path + ".html"), base / (path + ".html"),
                 ROOT / path / "index.html"]
    for c in cand:
        try:
            if c.exists():
                return "ok"
        except OSError:
            pass
    return "missing"


out = {"pages": {}, "global": {}}
anchors = {}

for name in PAGES:
    path = ROOT / name
    html = path.read_text(encoding="utf-8", errors="replace")
    c = Collector()
    c.feed(html)
    anchors[name] = set(c.ids)
    h1 = [h for h in c.headings if h["level"] == 1]
    jumps, prev = [], 0
    for h in c.headings:
        if prev and h["level"] > prev + 1:
            jumps.append(f"H{prev}->H{h['level']}: {h['text'][:50]}")
        prev = h["level"]
    lang = re.search(r'<html[^>]*\blang="([^"]*)"', html)
    missing = sorted({l["href"] for l in c.links
                      if target_exists(path, l["href"]) == "missing"})
    out["pages"][name] = {
        "title": c.title.strip(),
        "title_len": len(c.title.strip()),
        "description": c.metas.get("description", ""),
        "desc_len": len(c.metas.get("description", "")),
        "og_image": c.metas.get("og:image", ""),
        "lang": lang.group(1) if lang else "MISSING",
        "h1": [h["text"] for h in h1],
        "heading_count": len(c.headings),
        "heading_jumps": jumps,
        "dup_ids": [i for i, n in Counter(c.ids).items() if n > 1],
        "img_total": len(c.images),
        "img_no_alt_attr": sorted({i["src"] for i in c.images if i["alt"] is None}),
        "img_empty_alt": sorted({i["src"] for i in c.images if i["alt"] == ""}),
        "img_missing_file": sorted({i["src"] for i in c.images
                                    if target_exists(path, i["src"]) == "missing"}),
        "links_total": len(c.links),
        "links_missing": missing,
        "buttons": c.buttons,
        "svg": c.svg_count,
        "inline_scripts": c.scripts,
        "inline_styles": c.styles,
        "iframes": c.iframes,
        "outline": c.headings,
    }

for name in PAGES:
    path = ROOT / name
    html = path.read_text(encoding="utf-8", errors="replace")
    c = Collector()
    c.feed(html)
    bad = []
    for l in c.links:
        href = l["href"]
        if "#" not in href:
            continue
        base, frag = href.split("#", 1)
        if not frag:
            continue
        if base in ("", name):
            if frag not in anchors[name]:
                bad.append(href)
        else:
            tgt = base if base.endswith(".html") else base + ".html"
            tgt = Path(tgt).name
            if tgt in anchors and frag not in anchors[tgt]:
                bad.append(href)
    out["pages"][name]["anchors_missing"] = sorted(set(bad))

sm = (ROOT / "sitemap.xml").read_text(encoding="utf-8", errors="replace")
locs = re.findall(r"<loc>([^<]+)</loc>", sm)
out["global"]["sitemap_urls"] = len(locs)
out["global"]["sitemap_en"] = sorted(
    u for u in locs if not any(f"/{x}/" in u for x in LOCALES))
locale_hits = Counter()
for u in locs:
    tail = u.split("pvega62.github.io/", 1)[-1]
    seg = tail.split("/")[0]
    if seg in LOCALES:
        locale_hits[seg] += 1
out["global"]["sitemap_locales"] = dict(locale_hits)
out["global"]["sitemap_has_root"] = "https://pvega62.github.io/" in locs

Path(ROOT / "scratch" / "html-audit.json").write_text(
    json.dumps(out, indent=1, ensure_ascii=False), encoding="utf-8")
print("WROTE scratch/html-audit.json")
for p, d in out["pages"].items():
    print(f"{p}: h1={len(d['h1'])} h={d['heading_count']} imgs={d['img_total']} "
          f"noalt={len(d['img_no_alt_attr'])} emptyalt={len(d['img_empty_alt'])} "
          f"missingimg={len(d['img_missing_file'])} links={d['links_total']} "
          f"dead={len(d['links_missing'])} badanchor={len(d['anchors_missing'])} "
          f"dupids={len(d['dup_ids'])} jumps={len(d['heading_jumps'])} tl={d['title_len']} dl={d['desc_len']}")
