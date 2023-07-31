import bisect
import random
import time


def solution_2(n, arr):

    arr = [2, 4]

    def lbin(l=0, r=len(arr), find=3):

        while l < r:
            mid = (l+r) // 2
            if arr[mid] >= find:
                r = mid
            else:
                l = mid + 1

        return l

    f = 3
    print('ind:', lbin(find=3), 'f:', f, arr)

    def rbin(l=0, r=len(arr)-1, find=3):

        while l < r:
            mid = (l+r+1) // 2
            if arr[mid] <= find:
                l = mid
            else:
                r = mid - 1

        return l

    print('ind:', rbin(find=3), 'f:', f, arr)


def solution(n, arr):

    # ans = [0]
    ans = []
    for i in range(1, n-1):
        if arr[i-1] < arr[i] and arr[i] > arr[i+1]:
            ans.append(i+1)
            break

    return ans[0] if ans else 0
    # return set(ans)


def solution_3(n, arr):

    l = 1
    r = len(arr)-2
    while l < r:
        mid = (l+r) // 2
        if arr[mid] >= arr[mid+1]:
            r = mid
        else:
            l = mid + 1
    # print(arr)
    return l+1 if arr[l-1] < arr[l] and arr[l] > arr[l+1] else 0


if __name__ == '__main__':
    # n = int(input())
    # arr = list(map(int, input().split()))
    # print(solution_3(n, arr))
    # print(solution(n, arr))

    n = 10_000
    arr = list(range(1, n))
    arr.append(n-2)
    # print(arr)
    t = time.time()
    solution_3(n, arr)
    # solution(n, arr)
    print(time.time() - t, '(s)')

    # cnt = 0
    # while cnt != 100_000:
    #     n = random.randint(3, 10)
    #     arr = [random.randint(1, 100) for _ in range(n)]
    #     res = solution_3(n, arr)
    #     peak = solution(n, arr)
    #     assert res in peak, f'{arr}, res: {res}, peak:{peak}'
    #     cnt += 1
