L = int(input())
N = int(input())

t = []
cnt = 0
for _ in range(N):
    s = input()
    t += list(s) + ["\n"]
    cnt += len(s)

    if cnt >= L:
        # print(f'{t=}')
        cnt = 0
        for i in range(len(t)):
            if t[i] == "\n":
                continue

            cnt += 1
            if cnt == L - 3 and L > 3:
                t = t[: i + 1] + ["..."]
                break

            if cnt == L and L <= 3:
                t = t[: i + 1]
                break

# print(f'{t=}')
s = ""
for ch in t:
    if ch != "\n":
        s += ch
    else:
        print(s)
        s = ""

print(s)
