import numpy as np


def snake(m, n, direction="H"):
    order = "C" if direction == "H" else "F"
    a = np.arange(1, n * m + 1, dtype="int16").reshape(n, m, order=order)
    if direction == "H":
        for i in range(n):
            if i % 2 != 0:
                a[i] = a[i][::-1]
    if direction == "V":
        for j in range(m):
            if j % 2 != 0:
                a[:, j] = a[:, j][::-1]

    return a


if __name__ == "__main__":
    print(snake(5, 3))
    print(snake(5, 3, direction="V"))
