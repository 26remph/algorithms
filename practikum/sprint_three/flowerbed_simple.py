from typing import Dict

flowerbeds: Dict[int, int] = {}

n = int(input())
for _ in range(n):
    cut = list(map(int, input().split(' ')))
    key = cut[0]
    narrow_end = cut[1]

    if flowerbeds.get(key) is None:
        flowerbeds[key] = narrow_end
    else:
        flowerbeds[key] = max(flowerbeds[key], narrow_end)

flowerbeds = dict(sorted(flowerbeds.items()))
# print(flowerbeds)

start = next(iter(flowerbeds))
end = flowerbeds[start]
for key, val in flowerbeds.items():

    if key <= end:
        end = max(end, val)
    else:
        print(start, end)
        start = key
        end = val

print(start, end)


