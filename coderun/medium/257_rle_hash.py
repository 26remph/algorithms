import time

from string import ascii_lowercase


def main():
    s = input()
    q = int(input())

    t = time.time()
    size = len(s)
    base = round(len(s), -1)

    # num_s = ''
    # for i in range(len(s)):
    #     if s[i] in ascii_lowercase:
    #         if num_s:
    #             size += int(num_s)
    #             num_s = ''
    #         else:
    #             size += 1
    #     else:
    #         num_s += s[i]

    print('size', f'{size:,d}', 'base', base)

    harr = [[] for _ in range(size)]  # [start, end, len]
    # pref = [[0, 0, 0] for _ in range(size)]  # [start, end, len]

    print('init=', harr)
    # print('init=', pref)

    num_s = ''
    ind = 1
    size = 1
    for i in range(len(s)):

        if s[i] in ascii_lowercase:

            if num_s:
                size += int(num_s)

                harr[size % base].append((num_s + s[i], size))

                # pref[j][0] = pref[j-1][1] + 1
                # pref[j][1] = pref[j-1][1] + num
                # pref[j][2] = pref[j-1][2] + len(str(num)) + 1
                num_s = ''

            else:
                harr[size % base].append((s[i], size))
                # pref[j][0] = pref[j-1][1] + 1
                # pref[j][1] = pref[j][0]
                # pref[j][2] = pref[j-1][2] + 1
                size += 1

        else:
            num_s = ''.join([num_s, s[i]])

    print('fill=', harr)
    print('size', size)
    # print('fill=', pref)
    tpref = time.time() - t
    print(tpref, '(s)')

    t = time.time()
    # out = []
    #
    for _ in range(q):
        i, j = map(int, input().split())
        print(i, '=', harr[i % base])
        print(j, '=', harr[j % base])
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
    tq = time.time() - t
    print(tq, '(s)')
    print(tpref + tq, '(s) all')

    # print(cash)
    # print('s', s)
    # print('\n'.join(out))


if __name__ == '__main__':
    main()
