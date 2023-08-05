from collections import defaultdict


def solution(s):

    wrd = defaultdict(int)
    for i in range(len(s)):
        wrd[s[i]] += 1

    return wrd


if __name__ == '__main__':
    s = input()
    print(solution(s))
