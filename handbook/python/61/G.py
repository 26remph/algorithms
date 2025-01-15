import numpy as np


def make_board(n):
    a = np.ones((n, n), dtype="int8")
    for i in range(n):
        for j in range(n):
            if (i % 2 != 0 and j % 2 == 0) or (i % 2 == 0 and j % 2 != 0):
                a[i, j] = 0

    return a


if __name__ == "__main__":
    N = 6
    print(make_board(N))
