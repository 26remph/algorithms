from sys import stdin

ans = set()
for row in stdin:
    words = row.rstrip().split()
    for w in words:
        if w.lower() == w[::-1].lower():
            ans.add(w)

print('\n'.join(sorted(list(ans))))
