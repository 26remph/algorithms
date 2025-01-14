import numpy as np


def g_mean(arr: list[float]) -> float:
    a = np.array(arr)
    return a.prod() ** (1.0 / len(arr))


array = list(map(float, input().split()))
print(g_mean(array))
