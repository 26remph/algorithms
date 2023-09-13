def merge(lst1: list, lst2: list):

    res = []
    i, j = 0, 0
    while i < len(lst1) or j < len(lst2):

        if not (i < len(lst1)):
            return res + lst2[j:]

        if not (j < len(lst2)):
            return res + lst1[i:]

        if lst1[i] < lst2[j]:
            res.append(lst1[i])
            i += 1
        else:
            res.append(lst2[j])
            j += 1

    return res


if __name__ == '__main__':
    n = int(input())
    _ = input()
    arr1, arr2 = list(map(int, input().split())), []
    arr1.sort()
    for _ in range(n - 1):
        _ = input()
        arr2 = list(map(int, input().split()))
        arr2.sort()
        arr1 = merge(arr1, arr2)

    print(' '.join(map(str, arr1)))