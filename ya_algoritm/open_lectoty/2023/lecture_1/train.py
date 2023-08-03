SEC_IN_DAY = 24 * 60 * 60

n = int(input())
to_sec = lambda x: int(x.split(':')[0]) * 3600 + int(x.split(':')[1]) * 60
arrive = list(map(to_sec, input().split()))
arrive.sort()


min_sec = SEC_IN_DAY - arrive[-1] + arrive[0]
for i in range(1, len(arrive)):
    min_sec = min(arrive[i]-arrive[i-1], min_sec)

# print(arrive, min_sec, min_sec // 60, '(min)')
print(min_sec // 60)

