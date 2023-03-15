import heapq

_ = int(input())
arr = list(map(int, input().split(' ')))
heapq.heapify(arr)
ans = [heapq.heappop(arr) for _ in range(len(arr))]
print(*ans)

