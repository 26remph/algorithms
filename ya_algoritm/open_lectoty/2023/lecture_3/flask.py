import bisect


LIMIT_USEFUL = 2_000_001


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
                # useful += sum([x + arr[j] for x in arr[i:j]])
                pref = arr[j] * (j - i) + prefix[j] - prefix[i]
                useful += pref
                # print('sum:', sum([x + arr[j] for x in arr[i:j]]))
                # print('i', i, 'j', j)
                # print('prefix', prefix[j] - prefix[i])
                # print('prefix:', pref)
                # assert pref == sum([x + arr[j] for x in arr[i:j]])
                # prefix[j] - prefix[i]
                # j * i
                # assert False
            j -= 1
        else:
            i += 1

        # print('->', 'i', i, 'j', j, 'flask', flask, 'left', left)

    # unique  bottle
    i = bisect.bisect_right(arr, x)
    if i != len(arr):
        flask += len(arr) - i
        if is_ans:
            useful += prefix[len(arr)] - prefix[i]
            # useful += sum(arr[i:len(arr)])
            # assert prefix[len(arr)] - prefix[i] == sum(arr[i:len(arr)])

    return flask, useful


def bin_search(lo, hi):
    while lo < hi:
        mid = (lo + hi) // 2
        if produce_flask(mid)[0] <= k:
            hi = mid
        else:
            lo = mid + 1
    return lo


n, k = map(int, input().strip().split())
arr = list(map(int, input().strip().split()))

while True:
    # t = time.time()
    # print('---------')
    # n = random.randint(1, 5)
    # k = random.randint(1, n*(n+1) // 2)
    # arr = [random.randint(1, 10) for _ in range(n)]
    # print('gen arr', arr)
    # arr = list(set(arr))
    arr.sort()
    # print('set arr:', arr)

    # prefix summ
    # prefix = [0] * (len(arr) + 1)
    prefix = [0]
    for i in range(len(arr)):
        prefix.append(prefix[i] + arr[i])
        # prefix[i + 1] += prefix[i] + arr[i]
    # print('prefix:', prefix)

    # --- answer
    min_useful = bin_search(-LIMIT_USEFUL, LIMIT_USEFUL)
    # print('min_useful:', min_useful, 'k:', k)

    # t1 = time.time() - t
    # print('sort +bin: ->', t1, '(s)')

    ans = produce_flask(min_useful, is_ans=True)
    flask, total_useful = ans[0], ans[1]
    # print('flask:', flask, 'total_useful', totla_useful)

    ans_my = total_useful
    if min_useful != -LIMIT_USEFUL and flask < k:
        ans_my += (k - flask) * min_useful

    # print('optimize ->', ans_my)
    print(ans_my)
    # print(time.time() - t, '(s)')

    # --- sqrt solution
    out = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            out.append((arr[i], arr[j]))

    for i in range(len(arr)):
        out.append((0, arr[i]))

    out.sort(key=lambda x: x[0] + x[1])
    print("l=", len(out), "pair", out)

    _summ = [x[0] + x[1] for x in out]
    print("sum:", _summ)

    ans_sqrt = sum(_summ[-k:])
    print(ans_sqrt)

    assert ans_my == ans_sqrt, f"ans: {ans_my} -> {arr}, sqrt: {ans_sqrt} -> {out}"
    # assert False
