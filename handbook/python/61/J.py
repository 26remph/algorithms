import numpy as np


def stairs(vector: np.ndarray) -> np.ndarray:
    res = np.zeros((vector.size, vector.size), "int16")
    res[0] = vector
    for ii in range(1, vector.size):
        vector = np.concatenate([vector[-1:], vector[:-1]])
        res[ii] = vector

    return res


if __name__ == "__main__":
    print(stairs(np.arange(3)))
    print(stairs(np.arange(5)))
