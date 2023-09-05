N = int(input())
ans = []
for i in range(N):
    ans.append(int(input()))
p = int(input())
print('\n'.join(map(str, [pow(val, p) for val in ans])))
