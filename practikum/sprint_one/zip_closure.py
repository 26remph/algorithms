# from typing import List, Tuple
#
#
# # def zipper(a: List[int], b: List[int]) -> List[int]:
# #     # Здесь реализация вашего решения
# #     pass
#
# def read_input() -> Tuple[List[int], List[int]]:
#     n = int(input())
#     a = list(map(int, input().strip().split()))
#     b = list(map(int, input().strip().split()))
#     return a, b
#
#
# a, b = read_input()
# for elem in zip(a, b):
#     print(elem[0], elem[1], end=' ')
#
# # print(" ".join(map(str, zipper(a, b))))

from typing import List, Tuple


def read_input() -> Tuple[List[int], List[int]]:
    n = int(input())
    a = list(map(int, input().strip().split()))
    b = list(map(int, input().strip().split()))
    return a, b


a, b = read_input()
for elem in zip(a, b):
    print(elem[0], elem[1], end=' ')
