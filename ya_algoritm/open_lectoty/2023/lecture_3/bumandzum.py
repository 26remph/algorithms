import random
import time


# n = int(input())
# arr = list(map(int, input().split()))


while True:
    n = random.randint(100_000, 300_000)
    arr = [random.randint(1, 120) for _ in range(n)]

    t = time.time()

    arr.sort(reverse=True)
    ans = 0
    col = 0
    for ind in range(1, n):
        if arr[ind] == arr[ind - 1] and arr[ind] > arr[ind] * 0.5 + 7:
            col += 1
        else:
            ans += sum(range(1, col + 1))
            col = 0

    ans += sum(range(1, col + 1))
    # print('couple:', ans)

    i, j = 0, 1
    while i < n - 1:
        while j < n - 1 and arr[j + 1] > arr[i] * 0.5 + 7:
            j += 1
            # print('j_w ->', i, j)

        if arr[j] > arr[i] * 0.5 + 7:
            ans += j - i
            # print('j_i ->', i, j, 'ans:', ans)

        i += 1
        if i == j:
            j += 1

    print(time.time() - t, "(s)")
    print(ans)

    # ----
    # ans_3 = 0
    # for i in range(n):
    #     for j in range(i + 1, n):
    #         if arr[j] > arr[i] * 0.5 + 7:
    #             ans_3 += 2 if arr[j] == arr[i] else 1
    #
    # print(ans_3)
    # -----

    # assert ans_3 == ans, print('ans:', ans, 'ans_3:', ans_3, arr)
