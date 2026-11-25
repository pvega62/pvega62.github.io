"""Aggregate Vale JSON for the six English HTML pages."""

import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
data = json.loads((ROOT / "scratch" / "vale-html.json").read_text(encoding="utf-8"))

rows = []
for path, items in data.items():
    rel = Path(path).name
    for it in items:
        rows.append({
            "file": rel,
            "line": it["Line"],
            "col": (it.get("Span") or [0])[0],
            "sev": it["Severity"],
            "rule": it["Check"],
            "msg": it["Message"],
            "match": it.get("Match", ""),
        })

sev = Counter(r["sev"] for r in rows)
print("PAGES:", len(data), "FINDINGS:", len(rows), dict(sev))
print("\nBY SEVERITY x FILE")
for f in sorted({r["file"] for r in rows}):
    c = Counter(r["sev"] for r in rows if r["file"] == f)
    print(f"  {f:36s} E{c.get('error',0):4d} W{c.get('warning',0):4d} S{c.get('suggestion',0):4d}")

print("\nRULES (all)")
for rule, c in Counter(r["rule"] for r in rows).most_common():
    s = Counter(r["sev"] for r in rows if r["rule"] == rule)
    print(f"{c:5d}  {rule:38s} {dict(s)}")

print("\n=== AI-TELLS ===")
at = sorted([r for r in rows if r["rule"].startswith("ai-tells")],
            key=lambda r: (r["rule"], r["file"], r["line"]))
print("count:", len(at))
for r in at:
    print(f"{r['rule']}|{r['file']}|{r['line']}|{r['sev']}|{r['match'][:90]!r}")

print("\n=== ERRORS ===")
for r in sorted([r for r in rows if r["sev"] == "error"], key=lambda r: (r["file"], r["line"])):
    print(f"{r['file']}|{r['line']}|{r['rule']}|{r['msg'][:110]}|{r['match'][:60]!r}")

(ROOT / "scratch" / "html-detail.json").write_text(json.dumps(rows, indent=1), encoding="utf-8")
