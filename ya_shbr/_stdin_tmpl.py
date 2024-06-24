import time

from typing import Dict, List, Optional, Tuple


def foo(vacancy: Dict[str, int], arr: List[Tuple[str, str, int, int]]) -> List[str]:
    print(vacancy)
    print(arr)
    return ['anonymous', 'bill_gates', 'bjarne_stroustrup']


def read_input() -> Tuple[dict, list]:
    n = int(input())
    vacancy = {}
    for _ in range(n):
        name, capcity = input().strip().split(',')
        vacancy[name] = capcity
    k: int = int(input())
    arr = []
    for _ in range(k):
        candidate_id, vacancy_id, task, fine = input().strip().split(',')
        arr.append((candidate_id, vacancy_id, task, fine))
    return vacancy, arr


def print_result(result: Optional[Tuple[int, int]]) -> None:
    if result is None:
        print(None)
    else:
        print(" ".join(map(str, result)))


if __name__ == '__main__':
    vacancy, arr = read_input()
    start_time = time.time()
    # print(*foo(vacancy, arr))
    print('\n'.join(foo(vacancy, arr)))
    # print_result(foo(vacancy, arr))
    print("--- %s seconds ---" % (time.time() - start_time))