import collections


def markup(marks: list, letter: dict, limit: int):
    flag = False
    for val in letter.values():
        if val[0] < limit:
            for j in range(1, len(val)):
                marks[val[j]] = 0
                flag = True

    return flag


def solution(n, k, s):
    marks = []
    cnt = collections.Counter(s)
    for ch in s:
        marks.append(0 if cnt[ch] < k else 1)

    letter = collections.defaultdict(lambda: [0])  # [count, indexs]
    is_cont = True
    while is_cont:
        is_cont = False
        for i in range(n):
            if marks[i] > 0:
                letter[s[i]][0] += 1
                letter[s[i]].append(i)
            else:
                if markup(marks, letter, k):
                    is_cont = True
                letter.clear()

        if letter:
            if markup(marks, letter, k):
                is_cont = True
            letter.clear()

    ans, cnt = 0, 0
    for i in range(n):
        if marks[i] > 0:
            cnt += 1
        else:
            cnt = 0
        ans = max(ans, cnt)

    return ans


if __name__ == "__main__":
    n, k = map(int, input().split())
    s = input()
    print(solution(n, k, s))
