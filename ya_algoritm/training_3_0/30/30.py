n = int(input())
member_n = input().strip().split(' ')
m = int(input())
member_m = input().strip().split(' ')

dp = [[0 for _ in range(m+1)] for _ in range(n+1)]


for i in range(1, n+1):
    for j in range(1, m+1):
        if member_n[i-1] == member_m[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

i = n
j = m
ans = []
while i > 0 and j > 0:
    if dp[i][j] == dp[i-1][j]:
        i -= 1
    elif dp[i][j] == dp[i][j-1]:
        j -= 1
    else:
        # member = (member_n[i - 1], member_m[j - 1])
        ans.append(member_n[i-1])
        i -= 1
        j -= 1

print(*reversed(ans))
# print(member_m)
# print(member_n)
# for i in range(n+1):
#     print(f'{i}: {dp[i]}')


