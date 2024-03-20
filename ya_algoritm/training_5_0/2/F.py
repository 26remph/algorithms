import random

def rotate(ai, bi, arr):

    ai = ai % n
    bi = bi % n

    # print(f'rotate: {ai=}, {bi=}, {arr[ai: bi + 1]=}, {arr[ai:]=}, {arr[:bi+1]=}')
    if bi < ai:
        return max(arr[ai:] + arr[:bi+1])

    return max(arr[ai: bi + 1])


def solution(a, b, k, arr):
    ai, bi = 0, 0
    if a > k and a % k == 0:
        ai = a // k - 1
    elif a > k and a % k:
        ai = a // k

    if b > k and b % k == 0:
        bi = b // k - 1
    elif b > k and b % k:
        bi = b // k

    # print(f'{a=}, {b=}, {ai=}, {bi=}')

    if bi - ai >= n:
        return max(arr)

    win_to_right = rotate(ai, bi, arr)
    revers_arr = [arr[0]] + arr[:0:-1]
    win_to_left = rotate(ai, bi, revers_arr)

    # print(f'{win_to_right=}, {win_to_left=}')
    return max(win_to_right, win_to_left)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    a, b, k = map(int, input().split())
    print(solution(a, b, k, arr))

    # test system
    # for _ in range(100000):
    #     n = random.randint(3, 5)
    #     k = 1
    #     dimension = 4
    #     a = random.randint(1, n * dimension - 1)
    #     b = random.randint(a, n * dimension - 1)
    #     print(f'{a=}, {b=}')
    #     ai = a // k if a != k else 0
    #     bi = b // k if b != k else 0
    #     print(f'ind: {ai=}, {bi=}')
    #     arr = [random.randint(1, 10) for _ in range(n)]
    #     print(f'{arr=}')
    #     clone = []
    #     for _ in range(dimension):
    #         clone.extend(arr)
    #     res_r = max(clone[ai: bi + 1])
    #
    #     reverse_test_arr = [arr[0]] + arr[:0:-1]
    #     clone = []
    #     for _ in range(dimension):
    #         clone.extend(reverse_test_arr)
    #     res_l = max(clone[ai: bi + 1])
    #
    #     res = max(res_l, res_r)
    #     print(f'{reverse_test_arr=}, {a=}, {b=},{ai=}, {bi=}, {n=}, {res=}, {res_r=}, {res_l=}')
    #     print('-' * 50)
    #     ans = solution(a, b, k, arr)
    #     assert solution(a, b, k, arr) == res, f'{ans=}, {arr=}'
    #     print('--end--')
