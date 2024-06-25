M = int(input())

witness = []
for _ in range(M):
    witness.append(input())

N = int(input())
ans = []
max_cnt = 0
for pos in range(N):
    num = input()
    cnt = sum(1 for x in witness if set(x).issubset(num))
    max_cnt = max(cnt, max_cnt)
    ans.append((pos, num, cnt))

ans.sort(key=lambda x: (-x[2], x[0]))
for val in ans:
    if val[2] == max_cnt:
        print(val[1])

# print(set('BCDA').issubset('B137AC'))