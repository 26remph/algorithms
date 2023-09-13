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
    # l1 = [2, 5, 7, 8]
    # l2 = [3, 4, 6]
    # print(merge(lst1=l1, lst2=l2))
    lst = [7, 2, 5, 3, 7, 13, 1, 6]
    print(merge_sort(lst))


