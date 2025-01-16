import json


fn = "o.json"
with open(fn, encoding="UTF-8") as f:
    tests = json.load(f)

score = 0
for group in tests:
    points = group.get("points", 0)
    for t in group.get("tests", []):
        if t["pattern"] == input():
            score += int(points) / len(group["tests"])

print(int(score))
