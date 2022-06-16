from typing import List, Tuple

n: int = 0


def moving_average(arr: List[int], window_size: int) -> List[float]:

    sma: list = []
    sma_first = sum(arr[:window_size]) / window_size
    sma.append(sma_first)

    for i in range(n - window_size):
        sma_next = sma[i] - arr[i + 0] / window_size + arr[i + window_size] / window_size
        sma.append(sma_next)

    return sma


def read_input() -> Tuple[List[int], int, int]:
    n = int(input())
    arr = list(map(int, input().strip().split()))
    window_size = int(input())
    return arr, window_size, n


arr, window_size, n = read_input()
print(" ".join(map(str, moving_average(arr, window_size))))