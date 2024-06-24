def partition(a, lo, hi):

    pivot = a[lo]
    i = lo
    for j in range(lo + 1, hi):
        if a[j] <= pivot:
            i += 1
            if i != j:
                a[i], a[j] = a[j], a[i]
        else:
            order.append(a[j])

    a[lo], a[i] = a[i], a[lo]
    return i


if __name__ == '__main__':
    _ = int(input())
    arr = list(map(int, input().split()))
    order = []
    ind = partition(arr, 0, len(arr))
    # print(ind, arr, order)
    # print(' '.join(map(str, arr)))
    print(' '.join(map(str, arr[:ind + 1] + order)))
