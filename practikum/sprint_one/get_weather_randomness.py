from typing import List


def get_weather_randomness(temp: List[int]) -> int:

    _len = len(temp)
    if not _len:
        return 0
    if _len == 1:
        return 1

    rez: list = []
    if temp[0] > temp[1]:
        rez.append(temp[0])

    if temp[_len - 1] > temp[_len - 2]:
        rez.append(temp[_len - 1])

    for ind in range(1, _len - 1):
        if temp[ind] > temp[ind - 1] and temp[ind] > temp[ind + 1]:
            rez.append(temp[ind])

    return len(rez)


def read_input() -> List[int]:
    _ = int(input())
    temperatures = list(map(int, input().strip().split()))
    return temperatures


temperatures = read_input()
print(get_weather_randomness(temperatures))