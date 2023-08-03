def solution(n):

    cnt = 0
    for _ in range(n):
        flag = False
        while (s := input()) != 'ВСЁ':
            if s == 'зайка':
                flag = True

        cnt += 1 if flag else 0

    return cnt


if __name__ == '__main__':
    N = int(input())
    print(solution(N))