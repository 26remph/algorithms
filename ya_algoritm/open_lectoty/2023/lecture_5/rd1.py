import collections


d = collections.defaultdict(lambda: [0])

d["a"][0] += 1
d["a"].append(1)
d["a"].append(2)
print(d)
d.clear()

d["a"][0] += 1
d["a"][0] += 2
d["a"].append(6)

print(d)
