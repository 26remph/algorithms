import random

def partition(array, pivot):

    left, right, = 0, len(array) - 1
    # print('l,r', left, right)
    # print('pivot', pivot)
    while left < right:
        key_left = (array[left][1], array[left][2])
        key_right = (array[right][1], array[right][2])
        # print('key_left, key_right', key_left, key_right)

        if key_left <= pivot:
            left += 1
            continue

        if key_right > pivot:
            right -= 1
            continue
        
        array[left], array[right] = array[right], array[left]
        left += 1
        # right -= 1
        # print('array', array)

    return array[0: left], array[right: len(array)]

    # left = элементы array, меньшие pivot
    # center = элементы array, равные pivot
    # right = элементы array, большие pivot
    # return left, center, right
    # pass

def quicksort(array):
    if len(array) < 2:  # базовый случай,
        return array       # массивы с 0 или 1 элементами фактически отсортированы
    else:  # рекурсивный случай
        rnd = random.choice(array)
        pivot = rnd[1], rnd[2]
        # left, center, right = partition(array, pivot)
        left, right = partition(array, pivot)
        # print('quicksort', left, right)
        # return quicksort(left) + center + quicksort(right)
        return quicksort(left) + quicksort(right)

def read_input():
    n = int(input())
    arr = []
    for _ in range(n):
        row = input().split(' ')
        score = (row[0], int(row[1]), int(row[2]))
        arr.append(score)
    return arr

participants = read_input()
# print(participants)

# participants = quicksort(participants)
# print(participants)
# print((1, 1) <= (1, 2))
for write in quicksort(participants):
    print(write[0])


