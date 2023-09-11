def hanoi(n, A, C, B):
    if n != 0:
        hanoi(n - 1, A, B, C)
        print(A, '->', C)
        hanoi(n - 1, B, C, A)


hanoi(3, 'A', 'B', 'C')
