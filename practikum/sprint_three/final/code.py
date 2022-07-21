def binary_search(arr, x, left, right):

    if right <= left:
        return -1

    mid = (left + right) // 2
    if arr[mid] == x:
        return mid
    elif x < arr[mid]:
        return binary_search(arr, x, left, mid)
    else:
        return binary_search(arr, x, mid + 1, right)

def broken_search(nums, target) -> int:
    #  Your code
    #  “ヽ(´▽｀)ノ”
    if not nums:
        return -1

    ind = 0
    if nums[ind] == target:
        return 0
    
    for ind in range(1, len(nums)):
        if nums[ind] == target:
            return ind

        if nums[ind - 1] < nums[ind]:
            continue
        break

    if ind == 0:
        return -1

    offset = binary_search(nums, target, ind, len(nums))
    return offset

def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6
    arr = [5, 1]
    assert broken_search(arr, 1) == 1
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    assert broken_search(arr, 11) == 10
    arr = []
    assert broken_search(arr, 2) == -1
    arr = [0]
    assert broken_search(arr, 2) == -1
    arr = [0, 1]
    assert broken_search(arr, 1) == 1
    arr = [0]
    assert broken_search(arr, 0) == 0

if __name__ == '__main__':
    test()
