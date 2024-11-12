import time

from array import array
from string import ascii_lowercase


def main():
    # s = input() * 125_000
    s = input()
    _ = int(input())

    t = time.time()

    # size = 0
    # for i in range(len(s)):
    #     if s[i] in ascii_lowercase:
    #         size += 1

    arr = array("L", [0])
    # pref = [[0, 0, 0] for _ in range(size+1)]  # [start, end, len]

    num_s = ""
    j = 1

    print("init=", arr)
    for i in range(len(s)):
        if s[i] in ascii_lowercase:
            if num_s:
                num = int(num_s)
                arr.append(j)
                j += num - 1
                arr.append(j)
                # pref[j][0] = pref[j-1][1] + 1
                # pref[j][1] = pref[j-1][1] + num
                # pref[j][2] = pref[j-1][2] + len(str(num)) + 1
                num_s = ""

            else:
                arr.append(j)
                # pref[j][0] = pref[j-1][1] + 1
                # pref[j][1] = pref[j][0]
                # pref[j][2] = pref[j-1][2] + 1

            j += 1

        else:
            num_s = "".join([num_s, s[i]])

    print("fill=", arr)
    tpref = time.time() - t
    print(tpref, "(s)")

    # t = time.time()
    # out = []
    #
    # for _ in range(q):
    #     # i, j = map(int, input().split())
    #
    #     i = random.randint(1, pref[-1][1])
    #     j = random.randint(i, pref[-1][1])
    #
    #     start = bisect_left(pref, i,
    #                         key=lambda x: i if x[0] <= i <= x[1] else x[0])
    #
    #     end = bisect_left(pref, j,
    #                       key=lambda x: j if x[0] <= j <= x[1] else x[1])
    #
    #     if start == end:
    #         ans = (len(str(j - i + 1)) + 1) if j - i > 0 else 1
    #         out.append(str(ans))
    #         # print(ans, 'start==end')
    #     else:
    #         middle = pref[end-1][2] - pref[start][2]
    #         left = len(str(pref[start][1] - i + 1)) + 1 if pref[start][1] - i > 0 else 1
    #         right = len(str(j - pref[end][0] + 1)) + 1 if j - pref[end][0] > 0 else 1
    #
    #         ans = middle + left + right
    #         # print(ans, '| m', middle, 'l', left, 'r', right, '|', start, end)
    #         out.append(str(ans))
    #
    # tq = time.time()-t
    # print(tq, '(s)')
    # print(tpref + tq, '(s) all')
    # print(cash)
    # print('s', s)
    # print('\n'.join(out))


if __name__ == "__main__":
    main()
