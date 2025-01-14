import numpy as np


def multiplication_matrix(n):
    res = np.zeros(n * n, dtype=int).reshape(n, n)
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            res[i - 1, j - 1] = i * j
    return res


if __name__ == '__main__':
    n = 5
    print(multiplication_matrix(n))
