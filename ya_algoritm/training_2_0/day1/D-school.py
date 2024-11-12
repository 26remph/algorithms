def target_v2(array, n):
    if n == 1:
        return array[0]
    elif n == 2:
        return max(array)

    agr = [0] * n

    sumL = abs(array[0])
    agr[0] = abs(array[0])
    for i in range(1, n):
        agr[i] += abs(array[i]) + sumL
        sumL = agr[i]

    sumR = arr[-1]
    ans = (abs(sumR - agr[-1]), len(arr) - 1)
    for i in range(n - 2, -1, -1):
        sumR += abs(array[i])
        if abs(sumR - agr[i]) < ans[0]:
            ans = (abs(sumR - agr[i]), i)

    return array[ans[1]]


def target_v3(array, n):
    return array[n // 2]


# def target(array, n):
#
#     if n == 1:
#         return array[0]
#     elif n == 2:
#         return max(array)
#
#     i, j = 0, n - 1
#     sumL = abs(array[i])
#     sumR = abs(array[j])
#     ans = [0] * n
#
#     while i < j:
#
#         if sumL < sumR:
#             ans[i], ans[j] = abs(sumL), abs(sumR)
#             i += 1
#             sumL += array[i]
#         elif sumL > sumR:
#             ans[i], ans[j] = abs(sumL), abs(sumR)
#             j -= 1
#             sumR += array[j]
#         else:
#             ans[i], ans[j] = abs(sumL), abs(sumR)
#             i += 1
#             j -= 1
#             sumL += array[i]
#             sumR += array[j]
#
#     # print('*')
#     # print(arr)
#     # print(ans)
#     # print(arr[i])
#
#     return arr[i]


N = int(input())
arr = list(map(int, input().split()))
print(target_v2(arr, N))
print(target_v3(arr, N))


arr = [1, 2, 3, 4]
assert target_v2(arr, len(arr)) == target_v3(arr, len(arr))

arr = [0, 1, 1]
assert target_v2(arr, len(arr)) == target_v3(arr, len(arr))

arr = [0, 0]
assert target_v2(arr, len(arr)) == target_v3(arr, len(arr))

arr = [0, 1, 2]
print("v2=", target_v2(arr, len(arr)))
print("v3=", target_v3(arr, len(arr)))
assert target_v2(arr, len(arr)) == target_v3(arr, len(arr))

arr = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
assert target_v2(arr, len(arr)) == target_v3(arr, len(arr))

arr = [-1, 0, 1]
assert target_v2(arr, len(arr)) == target_v3(arr, len(arr))

arr = [-3, -2, -1, 0, 1]
assert target_v2(arr, len(arr)) == target_v3(arr, len(arr))

arr = [0, 1, 1, 2, 3]
assert target_v2(arr, len(arr)) == target_v3(arr, len(arr))

arr = [-1]
assert target_v2(arr, len(arr)) == target_v3(arr, len(arr))

arr = [-4, -3, -2, -1]
assert target_v2(arr, len(arr)) == target_v3(arr, len(arr))
