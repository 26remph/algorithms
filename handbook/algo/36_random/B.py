import random


def partition(a, lo, hi):
    pivot = a[random.randint(lo, hi)]
    i = lo
    j = hi
    while True:
        while a[i] < pivot:
            i += 1
        while a[j] > pivot:
            j -= 1
        if i >= j:
            return j

        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1


def quicksort(a, lo, hi):
    if lo < hi:
        ind = partition(a, lo, hi)
        quicksort(a, lo, ind)
        quicksort(a, ind + 1, hi)


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    quicksort(arr, 0, n - 1)
    print(" ".join(map(str, arr)))
