"""Extract visible prose from an HTML page with source line numbers."""

import html
import re
import sys
from pathlib import Path

p = Path(sys.argv[1])
start = int(sys.argv[2]) if len(sys.argv) > 2 else 1
end = int(sys.argv[3]) if len(sys.argv) > 3 else 10**9
raw = p.read_text(encoding="utf-8").splitlines()

in_skip = 0
for i, line in enumerate(raw, 1):
    if i < start or i > end:
        continue
    stripped = re.sub(r"(?is)<script.*?</script>", "", line)
    stripped = re.sub(r"(?is)<style.*?</style>", "", stripped)
    if re.search(r"(?i)<(script|style)\b", line) and not re.search(r"(?i)</script>|</style>", line):
        in_skip += 1
        continue
    if re.search(r"(?i)</(script|style)>", line):
        in_skip = max(0, in_skip - 1)
        continue
    if in_skip:
        continue
    if re.search(r"(?s)<!--.*?-->", line):
        line = re.sub(r"(?s)<!--.*?-->", "", line)
    txt = re.sub(r"(?s)<[^>]+>", " ", stripped)
    txt = html.unescape(txt)
    txt = re.sub(r"\s+", " ", txt).strip()
    if len(txt) > 2:
        print(f"{i}: {txt[:400]}")
