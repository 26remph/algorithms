import bisect


LIMIT_USEFUL = 2_000_001


def produce_flask(x, useful=0, is_ans=False) -> tuple[int, int]:
    i, j = 0, len(arr) - 1
    flask = 0
    while i < j:
        # combination
        left = x - arr[j]
        if arr[i] > left:
            flask += j - i
            if is_ans:
                pref = arr[j] * (j - i) + prefix[j] - prefix[i]
                useful += pref
            j -= 1
        else:
            i += 1

    # unique  bottle
    i = bisect.bisect_right(arr, x)
    if i != len(arr):
        flask += len(arr) - i
        if is_ans:
            useful += prefix[len(arr)] - prefix[i]

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
# arr = list(set(arr))
arr.sort()

prefix = [0]
for i in range(len(arr)):
    prefix.append(prefix[i] + arr[i])

# --- answer
min_useful = bin_search(-LIMIT_USEFUL, LIMIT_USEFUL)

ans = produce_flask(min_useful, is_ans=True)
flask, total_useful = ans[0], ans[1]

ans_my = total_useful
if min_useful != -LIMIT_USEFUL and flask < k:
    ans_my += (k - flask) * min_useful

print(ans_my)
