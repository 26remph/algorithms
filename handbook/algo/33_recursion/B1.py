# Алгоритм Фрейма — Стюарта
if __name__ == '__main__':
    n = int(input())

    tkr_4 = {1: 1, 2: 3, 3: 5, 4: 9, 5: 13, 6: 17}
    # r = 4

    k = n - round(pow(2 * n + 1, 0.5)) + 1
    tkr_3 = pow(2, n - k) - 1

    # print(f'{r=}, {k=}, {n=}')
    # print(f'r=3, (n-k)={n-k} -> {tkr_3}')
    # print(f'T(k,r)={2 * tkr_4[k]}, T(n-k, r-1)={tkr_3}')
    print(2 * tkr_4[k] + tkr_3)