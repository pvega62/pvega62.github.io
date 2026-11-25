"""List findings from the current Vale run, minus a chosen rule."""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
src = sys.argv[1] if len(sys.argv) > 1 else "scratch/vale-new.json"
skip = set(sys.argv[2].split(",")) if len(sys.argv) > 2 else set()
data = json.loads((ROOT / src).read_text(encoding="utf-8"))
for path, items in data.items():
    name = path.replace("\\", "/").split("pvega62.github.io/")[-1]
    for it in items:
        if it["Check"] in skip:
            continue
        print(f"{name}:{it['Line']} [{it['Severity'][:4]}] {it['Check']}: "
              f"{it.get('Match', '')[:40]!r} | {it['Message'][:75]}")
