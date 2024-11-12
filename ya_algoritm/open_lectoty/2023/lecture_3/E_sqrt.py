n, k = map(int, input().strip().split())
arr = list(map(int, input().strip().split()))
arr.sort()

# --- sqrt solution
out = []
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        out.append((arr[i], arr[j]))

for i in range(len(arr)):
    out.append((0, arr[i]))

out.sort(key=lambda x: x[0] + x[1])
print("l=", len(out), "pair", out)

_summ = [x[0] + x[1] for x in out]
print("sum:", _summ)

ans_sqrt = sum(_summ[-k:])
print(ans_sqrt)
