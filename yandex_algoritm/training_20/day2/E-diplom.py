N = int(input())
arr = list(map(int, input().split()))

arr.sort()
need_time = sum(arr[:-1])

print(need_time)
