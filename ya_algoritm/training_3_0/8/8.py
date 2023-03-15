k = int(input())

arr = []
for _ in range(k):
    x, y = map(int, input().split(' '))
    arr.append((x, y))

arr.sort(key=lambda t: t[0])
max_x = arr[-1][0]
min_x = arr[0][0]
arr.sort(key=lambda i: i[1])
max_y = arr[-1][1]
min_y = arr[0][1]
print(min_x, min_y, max_x, max_y)