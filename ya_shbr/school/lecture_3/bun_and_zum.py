n = int(input())
arr = list(map(int, input().split()))

arr.sort(reverse=True)
ans = 0
col = 0
for ind in range(1, n):
    if arr[ind] == arr[ind-1] and arr[ind] > arr[ind] * 0.5 + 7:
        col += 1
    else:
        ans += sum(range(1, col+1))
        col = 0

ans += sum(range(1, col+1))

i, j = 0, 1
while i < n - 1:

    while j < n - 1 and arr[j+1] > arr[i] * 0.5 + 7:
        j += 1

    if arr[j] > arr[i] * 0.5 + 7:
        ans += j - i

    i += 1
    if i == j: j += 1

print(ans)

