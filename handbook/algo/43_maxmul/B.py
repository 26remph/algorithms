import random


def maxPairwiseProduct(a):
    m1 = a[0]
    m2 = a[1]
    cnt = 0

    if m2 > m1:
        m2, m1 = m1, m2
        cnt += 1

    for i in range(2, n):
        cnt += 1
        if a[i] > m1:
            m2, m1 = m1, a[i]
        else:
            cnt += 1
            if a[i] > m2:
                m2 = a[i]
    return m1 * m2, cnt


if __name__ == '__main__':
    n = int(input())
    col = 0
    arr = []
    gen = 0
    # match = 0
    while col <= n * 1.5 and gen != 100_000:
    # while gen != 100_000:
        arr = [random.randint(0, n) for x in range(n)]
        max_mul, col = maxPairwiseProduct(arr)
        # if col > n * 1.5: match += 1
        gen += 1

    # print('match', match / 100_000 * 100, '%')
    if gen == 100_000:
        print('No')
    else:
        print('Yes')
        print(' '.join(map(str, arr)))
        # print(f'{col=}')
