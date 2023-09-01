N = int(input())
cnt = 0
for _ in range(N):
    s = input().lower()
    cnt += s.count('зайка')
print(cnt)
