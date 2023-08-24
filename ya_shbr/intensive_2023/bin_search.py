def left_search(arr, num):
    l = 0
    r = len(arr)
    while l < r:
        mid = (l + r) // 2
        if arr[mid] >= num:
            r = mid
        else:
            l = mid + 1

    return l


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 10]
    ind = left_search(arr, 9)
    assert left_search(arr, 5) == 4