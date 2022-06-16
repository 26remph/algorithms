"""
Ближайший ноль.

Расчет минимальной дистанции
"""
# id 68972579
from typing import List


def calc_dist(street: List[int], min_dist: List[int], reverse=False) -> List[int]:
    """Рассчитывает минимальное расстояние до нулевого значения,
    в зависимости от направления обхода: прямой или обратный.
    """
    if reverse:
        params = (len(street) - 1, -1, -1)
    else:
        params = (0, len(street), 1)

    skip = True
    zero_point: int = 0
    for ind in range(*params):
        if not skip and street[ind] > 0:
            min_dist[ind] = min(abs(zero_point - ind), min_dist[ind])

        if street[ind] == 0:
            min_dist[ind] = 0
            zero_point = ind
            skip = False

    return min_dist


def get_dist(street: List[int]) -> List[int]:
    """Алгоритм O(2n) сложности. Работает в два прохода. Прямой - для расчета
     первого приближения минимальных расстояний к нулевым точкам массива
     `street`. Обратный - уточняющий минимальные расстояния до нулевых точек
     массиа `street`.
     """
    min_dist: list = [len(street)] * len(street)
    min_dist = calc_dist(street, min_dist)
    min_dist = calc_dist(street, min_dist, reverse=True)

    return min_dist


def read_input() -> List[int]:
    _ = int(input())
    street = list(map(int, input().strip().split()))
    return street


streets = read_input()
print(" ".join(map(str, get_dist(streets))))
