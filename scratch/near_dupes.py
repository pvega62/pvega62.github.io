"""Catch typos that a dictionary cannot: one word spelled two ways.

Builds a frequency table over every string on the English pages, then reports
  - pairs one edit apart (e.g. Culangex / Culanex)
  - case variants of the same word (e.g. EQTemp / EQtemp)
with both forms actually present in the text.
"""
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

mapping = json.loads(Path('scratch/typo-map.json').read_text(encoding='utf-8'))
lines = Path('scratch/typo-probe.txt').read_text(encoding='utf-8').split('\n')

counts = Counter()
first_seen = {}
for idx, text in enumerate(lines, start=1):
    src = mapping.get(str(idx), {})
    where = f"{src.get('page')}:{src.get('line')}"
    for m in re.finditer(r"[A-Za-z][A-Za-z'\u2019-]{2,}", text):
        w = m.group(0)
        counts[w] += 1
        first_seen.setdefault(w, where)


def lev1(a, b):
    """True when a and b differ by exactly one insert, delete, or substitute."""
    if a == b:
        return False
    la, lb = len(a), len(b)
    if abs(la - lb) > 1:
        return False
    if la > lb:
        a, b, la, lb = b, a, lb, la
    i = j = 0
    diff = 0
    while i < la and j < lb:
        if a[i] == b[j]:
            i += 1
            j += 1
            continue
        diff += 1
        if diff > 1:
            return False
        if la == lb:
            i += 1
            j += 1
        else:
            j += 1
    return True


print('=== one-edit-apart pairs ===')
words = [w for w in counts if len(w) >= 4]
words.sort()
seen = set()
for a in words:
    for b in words:
        if a >= b:
            continue
        if not lev1(a.lower(), b.lower()):
            continue
        if abs(counts[a] - counts[b]) < 1:
            continue
        key = tuple(sorted((a.lower(), b.lower())))
        if key in seen:
            continue
        seen.add(key)
        rare, common = (a, b) if counts[a] <= counts[b] else (b, a)
        print(f'  {rare!r} ({counts[rare]}x, {first_seen[rare]})  vs  '
              f'{common!r} ({counts[common]}x, {first_seen[common]})')

print('\n=== case variants ===')
by_lower = defaultdict(set)
for w, c in counts.items():
    by_lower[w.lower()].add(w)
for low, forms in sorted(by_lower.items()):
    if len(forms) > 1:
        print(f'  {low}: ' + ', '.join(f'{f} ({counts[f]}x)' for f in sorted(forms)))

print('\n=== capitalization singles check ===')
print(f'total distinct words: {len(counts)}')
print('hapax legomena (appear once):')
for w, c in sorted(counts.items(), key=lambda kv: kv[0].lower()):
    if c == 1 and re.search(r'[A-Za-z]{4,}', w):
        print(f'  {w!r}  {first_seen[w]}')
