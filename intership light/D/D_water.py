n = int(input())
data = []
for _ in range(n):
    data.append(tuple(map(int, input().split())))

print(data)

start_ind = sorted(data, key=lambda x: (x[0], x[1]))
end_ind = sorted(data, key=lambda x: (x[1], x[0]))
print('start:', start_ind)
print('end:', end_ind)

q = int(input())


def binsearch(arr: list, ind: int, x: int, left, right) -> int:

    if right <= left:
        print('x, left, right:', x, left, right)
        return right
    mid = (left + right) // 2
    if arr[mid][ind] == x:
        while mid - 1 >= 0:
            if arr[mid - 1][ind] == x:
                mid -= 1
            else:
                break
        return mid
    elif x < arr[mid][ind]:
        # print(f'x {x}< {arr[mid][1]}:', left, right, mid, arr)
        return binsearch(arr, ind, x, left, mid)
    else:
        # print(f'x {x} > {arr[mid][1]}:', left, right, mid, arr)
        return binsearch(arr, ind, x, mid + 1, right)


for _ in range(q):
    row = list(map(int, input().split()))
    start, end, _type = row

    source = end_ind if _type == 2 else start_ind

    print(start, end)
    print('source:', source)
    search_ind = 1 if _type == 2 else 0
    ind = binsearch(source, search_ind, start, 0, len(source))
    print('ind', ind)

    sum_day = 0
    for pos in range(ind, len(source)):

        if source[pos][search_ind] > end:
            print('--> break')
            break

        if _type == 2:
            sum_day += source[pos][1] - source[pos][0]
        else:
            sum_day += source[pos][2]

    print('sum:', sum)
