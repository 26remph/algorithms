# ID 69517242
import random


def partition(array, pivot):
    (
        left,
        right,
    ) = 0, len(array) - 1
    while left < right:
        key_left = (array[left][1], array[left][2])
        key_right = (array[right][1], array[right][2])
        name_left, name_right = array[left][0], array[right][0]

        if key_left > pivot:
            left += 1
            continue

        if key_right < pivot:
            right -= 1
            continue

        if key_left == key_right and name_left < name_right:
            left += 1
            continue

        array[left], array[right] = array[right], array[left]
        left += 1

    return array[0:left], array[right : len(array)]


def quicksort(array):
    if len(array) < 2:
        return array

    rnd = random.choice(array)
    pivot = rnd[1], rnd[2]
    left, right = partition(array, pivot)
    return quicksort(left) + quicksort(right)


def read_input():
    n = int(input())
    arr = []
    for _ in range(n):
        row = input().split()
        score = (row[0], int(row[1]), -int(row[2]))
        arr.append(score)
    return arr


if __name__ == "__main__":
    for write in quicksort(read_input()):
        print(write[0])
