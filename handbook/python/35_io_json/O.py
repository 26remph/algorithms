import json


fn = "o.json"
tests = json.load(open(fn, encoding="UTF-8"))

score = 0
for group in tests:
    points = group.get("points", 0)
    for t in group.get("tests", []):
        if t["pattern"] == input():
            score += int(points) / len(group["tests"])

print(int(score))
