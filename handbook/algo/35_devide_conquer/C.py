def merge(lst1, lst2):

    i, j = 0, 0
    res = []
    while i < len(lst1) and j < len(lst2):

        if lst1[i] < lst2[j]:
            res.append(lst1[i])
            i += 1
        else:
            res.append(lst2[j])
            j += 1

    while i < len(lst1):
        res.append(lst1[i])
        i += 1

    while j < len(lst2):
        res.append(lst2[j])
        j += 1

    return res


def merge_sort(arr):

    if len(arr) <= 1:
        return arr
    else:
        n = len(arr) // 2
        return merge(merge_sort(arr[:n]), merge_sort(arr[n:]))


if __name__ == '__main__':
    _ = input()
    arr = list(map(int, input().split()))
    print(' '.join(map(str, merge_sort(arr))))
