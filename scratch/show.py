"""Print Vale findings grouped by page, filtered by severity."""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
rows = json.loads((ROOT / "scratch" / "html-detail.json").read_text(encoding="utf-8"))

want = sys.argv[1] if len(sys.argv) > 1 else "error"
pages = sys.argv[2:] or sorted({r["file"] for r in rows})
for page in pages:
    sel = [r for r in rows if r["file"] == page and r["sev"] == want]
    print(f"===== {page} [{want}] {len(sel)} =====")
    for r in sorted(sel, key=lambda r: r["line"]):
        print(f"{r['line']}:{r['col']} {r['rule']}: {r['msg'][:100]} | {r['match'][:55]}")
    print()
