import math

from typing import List


def g_mean(arr: List[float]) -> float:
    return math.exp(math.fsum(math.log(x) for x in arr) / len(arr))


array = list(map(float, input().split()))
print(g_mean(array))
