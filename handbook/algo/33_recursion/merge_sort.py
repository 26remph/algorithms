from collections import deque


def merge_deq(arr1: deque, arr2: deque):
    result = deque()

    while arr1 or arr2:
        if not arr1:
            return result + arr2

        if not arr2:
            return result + arr1

        while arr1:
            if len(arr1) > 1 and arr1[0] == arr1[1]:
                arr1.popleft()
            else:
                break

        while arr2:
            if len(arr2) > 1 and arr2[0] == arr2[1]:
                arr2.popleft()
            else:
                break

        if arr1[0] < arr2[0]:
            result.append(arr1.popleft())
        else:
            if arr1[0] == arr2[0]:
                arr1.popleft()
            result.append(arr2.popleft())

    return result


def merge(arr1, arr2):
    res = []
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if i < len(arr1) - 1 and arr1[i] == arr1[i + 1]:
            i += 1
            continue

        if j < len(arr2) - 1 and arr2[j] == arr2[j + 1]:
            j += 1
            continue

        if arr1[i] < arr2[j]:
            res.append(arr1[i])
            i += 1
        elif arr1[i] == arr2[j]:
            res.append(arr1[i])
            i += 1
            j += 1
        else:
            res.append(arr2[j])
            j += 1

    while i < len(arr1):
        res.append(arr1[i])
        i += 1

    while j < len(arr2):
        res.append(arr2[j])
        j += 1

    return res


def merge_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    else:
        mid = n // 2
        return merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))


if __name__ == "__main__":
    test = (
        ([6], [6], [6]),
        ([1, 2], [1, 2], [1, 2]),
        ([1, 2, 3], [4, 5, 6], [1, 2, 3, 4, 5, 6]),
        ([], [1, 2], [1, 2]),
        ([1, 2], [], [1, 2]),
        ([], [], []),
        ([1, 1, 1], [1, 1, 1], [1]),
    )
    for lst1, lst2, ans in test:
        res = merge(lst1, lst2)
        assert res == ans, f"{res=}, {ans=}"

    res = merge_sort([3, 1, 0, 10, 10, 100, 100, 1])
    print(res)
    # print(merge_sort(lst1))
