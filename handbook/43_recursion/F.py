def merge(arr1, arr2) -> list:

    i, j = 0, 0
    res = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            res.append(arr1[i])
            i += 1
        elif arr1[i] > arr2[j]:
            res.append(arr2[j])
            j += 1
        else:
            res += arr1 + arr2
            i += 1
            j += 2

    if i < len(arr1):
        res += arr1[i:]
    if j < len(arr2):
        res += arr2[j:]

    return res


result = []


def merge_sort(arr):

    if len(arr) == 2:
        return result.extend(merge(arr[0], arr[1]))
    elif len(arr) > 2:
        merge_sort(arr[:len(arr) // 2])
        merge_sort(arr[len(arr) // 2:])

    return result.extend([arr[0]])


if __name__ == '__main__':
    result = []
    print('1', merge([1], [0]))
    print('2', merge([0], [1]))
    print('3', merge([0], []))
    print('4', merge([], [0]))
    print('5', merge([1], [1]))
    print('5', merge([2], [1]))
    a = [1]
    print(a[len(a) // 2:])
    print(a[:len(a) // 2])
    print(merge_sort([2, 1, 6, 2, 0, 0]))
