def merge(arr, lf, mid, rg):
    y = arr[lf:mid]
    z = arr[mid:rg]
    k = lf
    while (len(y) > 0) and (len(z) > 0):
        if y[0] > z[0]:
            arr[k] = z.pop(0)
        else:
            arr[k] = y.pop(0)
        k += 1

    for i in range(len(z)):
        arr[k + i] = z[i]
    for i in range(len(y)):
        arr[k + i] = y[i]
    # print(lf, rg)
    return arr[lf:rg]


def merge_sort(arr, lf, rg):
    print(arr, id(arr))
    if len(arr[lf:rg]) < 2:
        return arr[lf:rg]
    mid = lf + (rg - lf) // 2
    merge_sort(arr, lf, mid)
    merge_sort(arr, mid, rg)
    return merge(arr, lf, mid, rg)


def test():
    a = [1, 4, 9, 2, 10, 11]
    b = merge(a, 0, 3, 6)
    expected = [1, 2, 4, 9, 10, 11]
    assert b == expected

    c = [1, 4, 2, 10, 1, 2]
    print(c, id(c))
    merge_sort(c, 0, 6)
    print(c, id(c))
    expected = [1, 1, 2, 2, 4, 10]
    assert c == expected


if __name__ == "__main__":
    test()
