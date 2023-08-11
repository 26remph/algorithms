import random


def solution(times):

    h, m, sec = map(int, times[0].split(':'))
    last = h * 3600 + m * 60 + sec

    cnt = 1
    for i in range(1, len(times)):

        h, m, sec = map(int, times[i].split(':'))
        h * 3600 + m * 60 + sec

        if last < (h * 3600 + m * 60 + sec):
            last = h * 3600 + m * 60 + sec
            continue
        else:
            last = h * 3600 + m * 60 + sec
            cnt += 1

    return cnt


def sol(arr):

    h, m, sec = map(int, arr[0].split(':'))
    now = h * 3600 + m * 60 + sec

    cnt = 0
    for i in range(len(arr)):

        h, m, sec = map(int, arr[i].split(':'))
        if now >= h * 3600 + m * 60 + sec:
            cnt += 1

        now = h * 3600 + m * 60 + sec

    return cnt


if __name__ == '__main__':
    # n = int(input())
    # arr = []
    # for _ in range(n):
    #     arr.append(input().strip())

    arr = [input().strip() for _ in range(int(input()))]
    # print(solution(arr))
    print(sol(arr))

    # for _ in range(10_000):
    #     arr = []
    #     for _ in range(10):
    #         h1 = random.choice('012')
    #         h2 = random.choice('0123456789') if h1 != '2' else random.choice('0123')
    #
    #         m1 = random.choice('012345')
    #         m2 = random.choice('0123456789')
    #
    #         sec1 = random.choice('012345')
    #         seq2 = random.choice('0123456789')
    #
    #         t = f'{h1+h2}:{m1+m2}:{sec1+seq2}'
    #         arr.append(t)
    #
    #     # print(arr)
    #     assert solution(arr) == sol(arr), arr





