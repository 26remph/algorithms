import sys


def dfs(x, depht):
    global flag

    if not flag:
        return

    if depht > d:
        flag = False
        # ans.append(x)
        return

    x *= 10
    prefix = []
    for i in range(0, 9):
        if (x + i) % k == 0:
            prefix.append(x + i)

    if depht <= d:
        for p in prefix:
            dfs(p, depht + 1)


def main():
    x = n
    for _ in range(1, d + 1):
        x *= 10
        prefix = []
        for i in range(0, 9):
            if (x + i) % k == 0:
                prefix.append(x + i)

        if prefix:
            x = prefix[0]
        else:
            x = -1
            break

    return x


sys.set_int_max_str_digits(0)


def main_opt():
    suf = ""
    x = n * 10
    for _ in range(0, 2):
        for i in range(0, 9):
            if (x + i) % k == 0:
                suf += str(i)
                break
        if suf:
            x += int(suf)
        else:
            return -1

    if d == 1:
        return int(str(n) + suf[0])

    if len(suf) < 2:
        return -1

    return int(str(n) + suf[0] + "".join([suf[1] for _ in range(0, d - 1)]))


if __name__ == "__main__":
    n, k, d = map(int, input().strip().split())
    print(main_opt())
    # n, k, d = 2, 5, 100
    # n, k, d = 7, 2, 4
    # n, k, d = 21, 108, 2
    # n, k, d = 88, 26, 2
    # n, k, d = 775, 277, 1

    # print(timeit.timeit(main_opt, number=1))
    # while True:
    #     n, k, d = [random.randint(1, 1000) for _ in range(3)]
    #     res_m = main()
    #     res_opt = main_opt()
    #     assert res_m == res_opt, f'{n=}, {k=}, {d=}, {res_m}, {res_opt}'
    #     # n, k, d = 7, 2, 2
    #     # n, k, d = 2, 1, 3
    #
    #     sys.setrecursionlimit(20_000)
    #     sys.set_int_max_str_digits(0)
    #     ans = []
    #     flag = True
    #     dfs(n, 1)
    #     res_dfs = ans[-1] if ans else -1
    #     # print('dfs:', res_dfs)
    #     res_main = main()
    #     # print('main:', res_main)
    #     # assert res_dfs == main(), f'{n=}, {k=}, {d=}, {res_dfs=}, {res_main=}'
    #     assert not(res_dfs > 0 and res_main < 0)
    #     print('pass')
