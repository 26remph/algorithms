import bisect
import itertools
import random

LIMIT_USEFUL = 2_000_000

def produce_flask(x, useful=0, is_ans=False) -> tuple[int, int]:

    i, j = 0, len(arr) - 1
    flask = 0
    while i < j:

        # combination
        left = x - arr[j]
        # i = bisect.bisect_left(arr, left)
        if arr[i] > left:
            flask += j - i
            if is_ans:
                useful += sum([x + arr[j] for x in arr[i:j]])
                print('useful_1:', useful, arr[i:j], '+', arr[j], 'i:', i, 'j:', j)
            j -= 1
        else:
            i += 1

        # print('->', 'i', i, 'j', j, 'flask', flask, 'left', left)

    # unique  bottle
    i = bisect.bisect_right(arr, x)
    if i != len(arr):
        flask += len(arr) - i
        if is_ans:
            useful += sum(arr[i:len(arr)])
            print('useful_2:', useful, arr[i:len(arr)])

    # print('i', i, 'j', len(arr), 'flask', flask)

    return flask, useful


def bin_search(lo, hi):

    while lo < hi:
        mid = (lo + hi) // 2
        if produce_flask(mid)[0] <= k:
            hi = mid
        else:
            lo = mid + 1
    return lo


# n, k = map(int, input().strip().split())
# arr = list(map(int, input().strip().split()))
while True:

    print('next --------->')
    n, k = 5, 5
    arr = [random.randint(-10, 10) for _ in range(n)]

    arr.sort()
    print('gen arr', arr)
    arr = list(set(arr))
    arr.sort()
    print('set arr:', arr)

    # --- answer
    min_useful = bin_search(-LIMIT_USEFUL, LIMIT_USEFUL)
    print('min_useful:', min_useful, 'k:', k)
    ans = produce_flask(min_useful, is_ans=True)
    flask, totla_useful = ans[0], ans[1]
    print('flask:', flask, 'total_useful', totla_useful)

    ans_my = totla_useful
    if min_useful != -LIMIT_USEFUL:
        if flask < k:
            ans_my += (k - flask) * min_useful

    print(ans_my)


    # --- sqrt solution
    out = []
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            out.append((arr[i], arr[j]))

    print('sqrt ->')
    out = list(set(out))
    out.sort(key=lambda x: x[0] + x[1] if x[0] != x[1] else x[0])
    print(out)
    tmp = [x[0] + x[1] if x[0] != x[1] else x[0]for x in out]
    print(tmp)
    ans_sqrt = sum(tmp[-k:])
    print(ans_sqrt)

    assert ans_my == ans_sqrt, f'ans: {ans_my} -> {arr}, sqrt: {ans_sqrt} -> {out}'
