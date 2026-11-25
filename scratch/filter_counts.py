"""Compare each page's filter labels with the real data-category tags."""

import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

for name in ("articles.html", "technical-writing-hardware.html", "uxwriting.html"):
    html = (ROOT / name).read_text(encoding="utf-8", errors="replace")
    items = re.findall(r'data-category="([^"]*)"', html)
    counts = Counter()
    for it in items:
        for tag in it.split():
            counts[tag] += 1
    labels = re.findall(r'data-filter="([^"]*)"[^>]*>\s*([^<]*?)\s*(\d+)', html)
    print(f"== {name} ==")
    print("  tagged items:", len(items))
    print("  tag counts:", dict(counts))
    print("  filter labels:", labels)
    # visible filter markup
    for m in re.finditer(r'<button[^>]*data-filter="([^"]*)"[^>]*>(.*?)</button>', html, re.S):
        txt = re.sub(r"<[^>]+>", " ", m.group(2))
        txt = re.sub(r"\s+", " ", txt).strip()
        print(f"    filter={m.group(1)!r} -> {txt!r}")
    print()
