L, K = list(map(int, input().split()))
block = list(map(int, input().split()))

bench = [0] * L

for ind in block:
    bench[ind] = 1

# print('bench', bench)

ans = []

if len(bench) % 2 != 0 and bench[len(bench) // 2] != 0:
    ans.append(str(len(bench) // 2))
else:
    shift = 1 if len(bench) % 2 == 0 else 0
    i = len(bench) // 2 - shift
    while i >= 0:
        if bench[i] != 0:
            ans.append(str(i))
            break
        i -= 1

    shift = 1 if len(bench) % 2 != 0 else 0
    i = len(bench) // 2 + shift
    while i < len(bench):
        if bench[i] != 0:
            ans.append(str(i))
            break
        i += 1

print(' '.join(ans))
