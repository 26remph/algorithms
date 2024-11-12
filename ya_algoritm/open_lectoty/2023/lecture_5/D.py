from collections import defaultdict, deque


# def speed_test():
#     lim = 100_000
#     s = ''.join([random.choice(ascii_lowercase) for _ in range(lim)])
#
#     t = time.time()
#     cnt = 0
#     for ch in ascii_lowercase:
#         for i in range(len(s)):
#             cnt += 1
#
#     print(time.time() - t, '(s)')


# def solution_sqrt(s):
#
#     i, j = 0, len(s) - 1
#     marks = [1] * len(s)
#
#     cnt, ch = 0, s[0]
#     while i < len(s):
#
#         if s[i] == ch:
#             cnt += 1
#             marks[i] = 0
#             i += 1
#         else:
#             ch = s[i]
#             # print(s[i-1], cnt)
#             j = len(s) - 1
#             before = cnt
#             while i < j:
#                 if marks[j] > 0 and s[i-1] == s[j] and cnt > 0:
#                     marks[j] = 0
#                     cnt -= 1
#
#                 j -= 1
#
#             if cnt == before:
#                 marks[i-1] = 1
#                 break
#
#             cnt = 0
#
#     print(marks)
#
#     ans = [s[ind] for ind in range(len(s)) if marks[ind] > 0]
#     print(len(ans))
#     print(''.join(ans))


def solution_wa(s):
    node = defaultdict(deque)

    sub = []
    ch = s[0]
    for i in range(len(s)):
        if ch == s[i]:
            sub.append(i)
        else:
            node[s[i - 1]].append(list(sub))
            sub.clear()
            sub.append(i)
            ch = s[i]

    if sub:
        node[s[len(s) - 1]].append(list(sub))

    # pprint(node)

    ch = s[0]
    for i in range(len(s)):
        if ch == s[i]:
            continue
        else:
            deq = node[s[i - 1]]
            if not deq:
                continue
            pref = deq.popleft()

            col, before = len(pref), len(pref)
            while deq and col:
                deq.pop()
                col -= 1

            if col == before:
                node[s[i - 1]].append(pref)
                break

            ch = s[i]

    ans = 0
    col = sum(1 for val in node.values() if val)
    if col == 1:
        for val in node.values():
            if val and sum(len(v) for v in val) == 1:
                ans = 1
                break
    else:
        for val in node.values():
            ans += sum(len(v) for v in val)

    print(ans)
    # pprint(node)


def solution(s):
    if len(s) == 1:
        return 1

    i, j = 0, len(s) - 1

    while i < j:
        if s[i] == s[j]:
            ch = s[i]
            while i < j and s[i] == ch:
                i += 1

            while i < j and s[j] == ch:
                j -= 1

        else:
            break

    # print('i:', i, 'j:', j)
    ans = 0
    if j - i:
        ans = j - i + 1
    else:
        if s[i - 1] != s[j]:
            ans = 1

    return ans


if __name__ == "__main__":
    s = input().strip()
    print(solution(s))

    # while True:
    #     s = ''.join([random.choice(ascii_lowercase) for _ in range(10)])
    #     s = 'hgcgtcpihl'
    #     print(s)
    #     solution_sqrt(s)
    #     t = time.time()
    #     solution(s)
    #     print(time.time() - t, '(s)')
