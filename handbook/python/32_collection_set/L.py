from collections import defaultdict


n = int(input())
cnt = defaultdict(int)

for _ in range(n):
    cnt[input()] += 1

fio = list(cnt.keys())
fio.sort()
flag = True
for f in fio:
    col = cnt[f]
    if col > 1:
        flag = False
        print(f, "-", cnt[f])

if flag:
    print("Однофамильцев нет")
