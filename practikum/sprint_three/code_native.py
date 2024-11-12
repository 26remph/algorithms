def merge(arr, lf, mid, rg):
    left = arr[lf:mid]
    right = arr[mid:rg]

    l, r, k = 0, 0, lf
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            arr[k] = left[l]
            l += 1
        else:
            arr[k] = right[r]
            r += 1
        k += 1

    while l < len(left):
        arr[k] = left[l]
        l += 1
        k += 1
    while r < len(right):
        arr[k] = right[r]
        r += 1
        k += 1

    return arr[lf:rg]


def merge_sort(arr, lf, rg):
    if len(arr[lf:rg]) == 1:
        return arr[lf:rg]

    mid = lf + len(arr[lf:rg]) // 2
    merge_sort(arr, lf, mid)
    merge_sort(arr, mid, rg)

    return merge(arr, lf, mid, rg)


def test():
    a = [1, 4, 9, 2, 10, 11]
    b = merge(a, 0, 3, 6)
    expected = [1, 2, 4, 9, 10, 11]
    assert b == expected

    c = [1, 4, 2, 10, 1, 2]
    merge_sort(c, 0, 6)
    expected = [1, 1, 2, 2, 4, 10]
    assert c == expected


if __name__ == "__main__":
    test()
