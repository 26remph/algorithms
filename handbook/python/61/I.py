import numpy as np


def rotate(arr: np.ndarray, pi):
    n = pi / 90
    arr = np.rot90(arr, n, axes=(1, 0))
    return arr


if __name__ == "__main__":
    print(rotate(np.arange(12).reshape(3, 4), 90))
    print(rotate(np.arange(12).reshape(3, 4), 270))
