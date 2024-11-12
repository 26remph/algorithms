import json
import sys


fn = input()

with open(fn, "r+", encoding="UTF-8") as f:
    d = json.load(f)
    for line in sys.stdin:
        key, val = line.split("==")
        d: dict
        d[key.strip()] = val.strip()

    f.truncate()
    f.seek(0)
    json.dump(d, f, indent=4)
