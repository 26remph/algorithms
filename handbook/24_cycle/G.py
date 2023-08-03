def solution(n):

    st = 3
    cnt = 1
    while cnt < n + 1:

        for i in range(st, 0, -1):
            print(f'До старта {i} секунд(ы)')

        print(f'Старт {cnt}!!!')
        st += 1
        cnt += 1


if __name__ == '__main__':
    N = int(input())
    solution(N)