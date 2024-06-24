def binary_search(arr, x, left, right):

    if right <= left:
        return left

    mid = (left + right) // 2
    # print('ind_mid', mid, 'mid', arr[mid], 'left', left, 'right', right)
    if arr[mid] == x:
        # print('# центральный элемент — искомый')
        while arr[mid - 1] == x:
            mid -= 1
        return mid
    elif x < arr[mid]:
        # print('# значит следует искать в левой половине')
        return binary_search(arr, x, left, mid)
    else:
        # print('# иначе следует искать в правой половине')
        return binary_search(arr, x, mid + 1, right)


_ = int(input())
capital = list(map(int, input().split(' ')))
cost = int(input())

cash_available = capital[-1]

if cost * 2 <= cash_available:
    ind_two = binary_search(capital, cost * 2, left=0, right=len(capital))
else:
    ind_two = -1

# print('-' * 25)
if ind_two > -1:
    ind_one = binary_search(capital, cost, left=0, right=ind_two + 1)
elif cost <= cash_available:
    ind_one = binary_search(capital, cost, left=0, right=len(capital))
else:
    ind_one = -1

if ind_one > -1:
    ind_one += 1

if ind_two > -1:
    ind_two += 1

print(ind_one, ind_two)
