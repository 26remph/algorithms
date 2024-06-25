import random


def pref_sum():
    pref = [0] * (N + 1)
    for i in range(len(arr)):
        if (pref[i] + arr[i]) > 0:
            pref[i + 1] = pref[i] + arr[i]

    ans = max(pref[1:])
    if ans == 0:
        ans = max(arr)
    # print('*')
    # print(ans)
    # print(arr)
    # print(pref)

    return ans


def test_func(a):

    # n = int(input())
    # a = list(map(int, input().split()))
    s = 0
    mx = a[0]
    for i in a:
        s += i
        mx = max(mx, s)
        if s < 0:
            s = 0
        # print(s, end=' ')
    print('mx', mx)
    return mx

# N = int(input())
# arr = list(map(int, input().split()))
# N = 1
# arr = [-37]
# assert test_func(N, arr) == pref_sum(), f'arr: {arr}'


while True:
    N = random.randint(1, 10)
    arr = [random.randint(-100, 100) for _ in range(N)]
    assert test_func(arr) == pref_sum(), f'arr: {arr}'
