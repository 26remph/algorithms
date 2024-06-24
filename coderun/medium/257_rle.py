import random
import time

from bisect import bisect_left
from string import ascii_lowercase


def main():
    # s = input() * 125_000
    s = input() * 4
    q = int(input())

    t = time.time()

    # size = 0
    # for i in range(len(s)):
    #     if s[i] in ascii_lowercase:
    #         size += 1

    # pref = [[0, 0, 0] for _ in range(size+1)]  # [start, end, len]
    # pref: list[tuple[int, int, int]] = [(0, 0, 0)]  # len+1, [start, end, len]

    pref: list[list[tuple[int, int, int, int]]] = [[] for _ in range(2)]  # len+1, [start, end, len, abslen]
    pref[0].append((0, 0, 0, 0))
    num_s = ''
    letters = set(ascii_lowercase)

    # print('init=', pref)
    H = 10
    lim = 500_000
    h = 0
    prev = pref[0][0]
    for i in range(len(s)):

        if s[i] in letters:

            if num_s:
                num = int(num_s)
                # st, end = pref[h][j-1][1] + 1, pref[h][j-1][1] + num
                st, end = prev[1] + 1, prev[1] + num
                l1 = len(str(num)) + 1
                l = prev[2] + l1
                prev = (st, end, l, l1)

                if end > (h + 1) * H:
                    pref[h].append(prev)
                    h = end // H
                    pref[h].append(prev)
                else:
                    h = end // H
                    pref[h].append(prev)

                num_s = ''
                col += 1

            else:
                st = prev[1] + 1
                # st = pref[h][j-1][1] + 1
                # end, l = st, pref[h][j-1][2] + 1
                end = st
                l = prev[2] + 1
                prev = (st, end, l, 1)

                h = end // H
                pref[h].append(prev)

        else:
            num_s = ''.join([num_s, s[i]])

    # print('fill=', pref)
    tpref = time.time() - t
    print(tpref, '(s)')
    print('l=', l, 'len(arr)', len(pref))

    t = time.time()
    out = []

    for _ in range(q):
        # i, j = map(int, input().split())

        i = random.randint(1, l)
        j = random.randint(i, l)

        h1 = i // H
        start = bisect_left(pref[h1], i,
                            key=lambda x: i if x[0] <= i <= x[1] else x[0])

        h2 = j // H
        end = bisect_left(pref[h2], j,
                          key=lambda x: j if x[0] <= j <= x[1] else x[1])

        if start == end:
            ans = (len(str(j - i + 1)) + 1) if j - i > 0 else 1
            out.append(str(ans))
            # print(ans, 'start==end')
        else:
            # middle = pref[h][end-1][2] - pref[h][start][2]
            try:
                t0 = pref[h2][end][2]
                t1 = pref[h1][start][2]
            except IndexError:
                print('i, j', i, j)
                print('(h1, s)', h1, start, '(h2, e)', h2, end)

                print('h1', pref[h1], len(pref[h1]))
                print('h2', pref[h2], len(pref[h2]))
                print('pr', pref)

                return None

            t3 = pref[h2][end][3]
            middle = pref[h2][end][2] - pref[h1][start][2] - pref[h2][end][3]

            s_pos = pref[h1][start][1]
            left = len(str(s_pos - i + 1)) + 1 if s_pos - i > 0 else 1
            e_pos = pref[h2][end][0]
            right = len(str(j - e_pos + 1)) + 1 if j - e_pos > 0 else 1

            ans = middle + left + right
            # print(ans, '| m', middle, 'l', left, 'r', right, '|', start, end)
            out.append(str(ans))

    tq = time.time() - t
    print(tq, '(s)')
    print(tpref + tq, '(s) all')
    # print('s', s)
    # print('\n'.join(out))


if __name__ == '__main__':
    main()
