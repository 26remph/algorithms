def merge_sort(array):
    if len(array) == 1:
        return array

    left = merge_sort(array[0: len(array) // 2])
    right = merge_sort(array[len(array) // 2: len(array)])

    result = [None] * len(array)
    l, r, k = 0, 0, 0

    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            result[k] = left[l]
            l += 1
        else:
            result[k] = right[r]
            r += 1
        k += 1

    while l < len(left):
        result[k] = left[l]
        l += 1
        k += 1
    while r < len(right):
        result[k] = right[r]
        r += 1
        k += 1

    return result


s = input()
t = input()
srt_t = ''.join(merge_sort(list(t)))
print(srt_t)
print(s in srt_t)
