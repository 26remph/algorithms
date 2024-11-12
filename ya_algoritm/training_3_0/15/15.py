n = int(input())
arr = list(map(int, input().split(" ")))

stack = []
ans = [0] * len(arr)
for i in range(n):
    if not stack:
        stack.append((arr[i], i))
        continue

    while stack and (stack[-1][0] > arr[i]):
        val = stack.pop()
        ans[val[1]] = i

    stack.append((arr[i], i))

while stack:
    val = stack.pop()
    ans[val[1]] = -1

print(*map(str, ans))
