def merge_sort(array):
    if len(array) == 1:  # базовый случай рекурсии
        # print('exit', array)
        return array

    # print('arr:', len(array), array)
    # print('left index:', len(array) // 2)
    # print('right index:', (len(array) // 2))

    # запускаем сортировку рекурсивно на левой половине
    left = merge_sort(array[0: len(array) // 2])

    # запускаем сортировку рекурсивно на правой половине
    # print('right recurse run ....')
    # print('array after >', array)
    right = merge_sort(array[len(array) // 2: len(array)])

    # заводим массив для результата сортировки
    result = [None] * len(array)
    # print('-' * 25)
    # print('заводим массив для результата сортировки ....')
    # print('array >', array)
    # print('result >', result)
    # print('left >', left)
    # print('right >', right)

    # сливаем результаты
    l, r, k = 0, 0, 0
    while l < len(left) and r < len(right):
        # выбираем, из какого массива забрать минимальный элемент
        if left[l] <= right[r]:
            result[k] = left[l]
            l += 1
        else:
            result[k] = right[r]
            r += 1
        k += 1

    # Если один массив закончился раньше, чем второй, то
    # переносим оставшиеся элементы второго массива в результирующий
    while l < len(left):
        result[k] = left[l]  # перенеси оставшиеся элементы left в result
        l += 1
        k += 1
    # print('result > ', result)
    while r < len(right):
        # print('k, r, l', k, r, l)
        # print(result[k])
        # print(right[r])
        result[k] = right[r]  # перенеси оставшиеся элементы right в result
        # print('remove')
        r += 1
        k += 1

    return result

s = input()
t = input()
srt_t = ''.join(merge_sort(list(t)))
print(s in srt_t)
