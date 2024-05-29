n = int(input())
arr = []
for _ in range(n):
    arr += input().split(', ')
arr.sort()
for i, name in enumerate(arr, 1):
    print(f'{i}. {name}')