import itertools


def check_solution(arr, n, k):

    min_l = float('inf')
    for c in itertools.combinations(arr, n - k):
        min_l = min(min_l, max(c) - min(c))

    return min_l


def wrong_solution(arr, n, k):

    if n == 0 or n == 1:
        return 0

    arr.sort(reverse=True)
    step = k
    i = 0
    j = len(arr) - 1
    while i != j and step:
        if arr[i + 1] - arr[j] < arr[i] - arr[j - 1]:
            i += 1
            print(f'{i=}')
        else:
            j -= 1
            print(f'{j=}')

        step -= 1

    # assert j - i + 1 == n - k, f'{arr=}, {n=}, {k=}'
    print(f'{i=}, {j=}')
    return arr[i] - arr[j]


def solution(arr, n, k):

    if k == 0:
        return max(arr) - min(arr)

    arr.sort()
    # print(arr)
    min_l = float('inf')
    for i in range(n - k - 1, len(arr)):
        min_l = min(min_l, arr[i] - arr[i - (n - k - 1)])
        # print('i=', i, 'j=', i - (n - k - 1))

    return min_l


if __name__ == '__main__':
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(solution(arr, n, k))
    # test = (
    #     (10, 5, [9, 8, 6, 5, 5, 5, 5, 3, 1, 1], 1),
    #     (2, 0, [15, 19], 4),
    #     (7, 2, [1, 11, 6, 41, 15, 13, 14], 9),
    #     (2, 0, [7, 4], 3),
    #     (2, 1, [7, 4], 0),
    #     (2, 1, [7, 4], 0),
    #     (3, 1, [7, 4, 3], 1),
    #     (4, 1, [7, 7, 7, 7], 0),
    #     (3, 2, [7, 7, 7], 0),
    #     (3, 1, [7, 7, 3], 0),
    #     (4, 2, [7, 4, 3, 1], 1),
    #     (2, 0, [7, 1], 6),
    #     (1, 0, [8], 0),
    # )
    # for n, k, arr, ans in test:
    #     res = solution(arr, n, k)
    #     # print(res)
    #     assert res == ans, f'{res=}, {ans=}, {arr=}'
    #
    # while True:
    #     n = random.randint(1, 20)
    #     k = random.randint(0, n - 1)
    #     arr = [random.randint(1, 10) for _ in range(n)]
    #
    #     res_true = check_solution(arr, n, k)
    #     res_test = solution(arr, n, k)
    #     assert res_true == res_test, f'{arr=}, {n=}, {k=}, {res_test=}, {res_true=}'
    #
    #     print(f'check: {(n, k, arr)=}')
