from typing import List, Tuple, Optional, Dict
import time
from operator import itemgetter


def foo(vacancy: Dict[str, int], arr: List[Tuple[str, str, int, int]]) -> List[str]:
    print(vacancy)
    print(arr)
    staff: List[str] = []

    for name, capcity in vacancy.items():
        print('name, capcity:', name, capcity)
        filtered_vacancy = list(filter(lambda x: x[1] == name, arr))

        rez: list = sorted(filtered_vacancy, key=lambda x: (-x[2], x[3]))

        end: int = min(len(rez), capcity)
        names = [x[0] for x in rez[:end]]
        print('names=', names)
        staff = staff + names
        print('rez=', rez)
        print('staff=', staff)

    staff.sort()

    return staff


def read_input() -> Tuple[dict, list]:
    n = int(input())
    vacancy = {}
    for _ in range(n):
        name, capcity = input().strip().split(',')
        vacancy[name] = int(capcity)
    k: int = int(input())
    arr = []
    for _ in range(k):
        candidate_id, vacancy_id, task, fine = input().strip().split(',')
        arr.append((candidate_id, vacancy_id, int(task), int(fine)))
    return vacancy, arr


def print_result(result: Optional[Tuple[int, int]]) -> None:
    if result is None:
        print(None)
    else:
        print(" ".join(map(str, result)))


if __name__ == '__main__':
    vacancy, arr = read_input()
    start_time = time.time()
    print('\n'.join(foo(vacancy, arr)))
    print("--- %s seconds ---" % (time.time() - start_time))
