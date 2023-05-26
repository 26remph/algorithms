import sys


def main():

    s = input()
    C = input()
    t = set()

    if C in s:
        print(len(C))
        return

    min_len = len(s) + 1
    cnt = 0
    C = set(C)
    i = 0
    while i < len(s):
        ch = s[i]

        if ch in C:
            t.add(ch)
            cnt += 1
            if len(t) == len(C):
                min_len = min(cnt, min_len)
                i = i - cnt + 1

                cnt = 0
                t = set()
        else:
            cnt = 0
            t = set()

        i += 1

    print(0 if min_len == len(s) + 1 else min_len)


if __name__ == '__main__':
    main()
