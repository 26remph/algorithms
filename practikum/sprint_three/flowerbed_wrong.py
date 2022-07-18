from typing import Dict

flowerbeds: Dict[int, int] = {}

n = int(input())
# max_ind = -1
# max_end = -1
for _ in range(n):
    cut = list(map(int, input().split(' ')))
    key = cut[0]
    narrow_end = cut[1]

    # max_ind = max(max_ind, key)
    # max_end = max(max_end, narrow_end)

    if flowerbeds.get(key) is None:
        flowerbeds[key] = narrow_end
    else:
        flowerbeds[key] = max(flowerbeds[key], narrow_end)

flowerbeds = dict(sorted(flowerbeds.items()))
print(flowerbeds)

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



# ind = next(iter(flowerbeds))
# while ind <= max_ind:
#
#     if flowerbeds.get(ind) is None:
#         ind += 1
#         continue
#
#     narrow_end = flowerbeds[ind]
#     # print(max_ind, max_end)
#     if narrow_end > max_ind:
#         print(ind, max(narrow_end, max_end))
#         break
#
#     while flowerbeds.get(narrow_end) is not None:
#         narrow_end = flowerbeds[narrow_end]
#
#     print(ind, narrow_end)
#     ind = narrow_end



