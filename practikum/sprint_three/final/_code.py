# ID 69455473
def binary_search(arr, x, left, right):

    if right <= left:
        return -1

    mid = (left + right) // 2
    left_unsorted = arr[left] > arr[mid]
    right_unsorted = arr[mid] > arr[right - 1]
    if arr[mid] == x:
        return mid
    elif arr[left] <= x <= arr[mid]:
        return binary_search(arr, x, left, mid)
    elif arr[mid] < x <= arr[right - 1]:
        return binary_search(arr, x, mid + 1, right)
    elif left_unsorted:
        return binary_search(arr, x, left, mid)
    elif right_unsorted:
        return binary_search(arr, x, mid + 1, right)
    else:
        return -1


def broken_search(nums, target) -> int:

    if not nums:
        return -1

    ind = 0
    return binary_search(nums, target, ind, len(nums))


def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6
    arr = [5, 1]
    assert broken_search(arr, 1) == 1
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    assert broken_search(arr, 11) == 10
    arr = []
    assert broken_search(arr, 2) == -1
    arr = [0]
    assert broken_search(arr, 2) == -1
    arr = [0, 1]
    assert broken_search(arr, 1) == 1
    arr = [0]
    assert broken_search(arr, 0) == 0
    arr = [19, 21, 24, 100, 101, 200, 1, 7, 12]
    assert broken_search(arr, 1) == 6
    arr = [19, 21, 24, 100, 101, 200, 1, 7, 12]
    assert broken_search(arr, 12) == 8
    arr = [19, 21, 24, 100, 101, 200, 1, 7, 12]
    assert broken_search(arr, 21) == 1
    arr = [19, 21, 24, 100, 101, 200, 1, 7, 12]
    assert broken_search(arr, 7) == 7
    arr = [1, 2, 5, 6, 8, 9, 12, 14, 16]
    assert broken_search(arr, 12) == 6
    arr = [19, 2, 5, 6, 8, 9, 12, 14, 16]
    assert broken_search(arr, 12) == 6


if __name__ == '__main__':
    test()
