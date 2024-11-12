fn1, fn2, fn3 = input(), input(), input()
words1, words2 = set(), set()

with open(fn1, encoding="UTF-8") as f:
    for line in f:
        words1.update(line.split())

with open(fn2, encoding="UTF-8") as f:
    for line in f:
        words2.update(line.split())


ans = list(words1 ^ words2)
ans.sort()
fans = open(fn3, "w", encoding="UTF-8")
print("\n".join(ans), file=fans)
fans.close()
