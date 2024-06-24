import bisect


n = int(input())
arr = list(set(map(int, input().strip().split(' '))))
arr.sort()

k = int(input())
query = list(map(int, input().strip().split(' ')))

for num in query:
    ind = bisect.bisect_left(arr, num)
    print(ind)
