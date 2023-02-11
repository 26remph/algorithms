from typing import List, Tuple


def get_player(vacancy: dict, arr: List[Tuple[str, str, int, int]]) -> List[str]:

    staff: List[str] = []
    results = sorted(vacancy.items(), key=lambda x: x[0])
    arr.sort(key=lambda x: (x[1], -x[2], x[3]))

    for name, capacity in results:
        count: int = 0

        if not arr:
            break

        while count < len(arr) and arr[count][1] == name:
            if count < capacity:
                staff.append(arr[count][0])
            count += 1

        del arr[:count]

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
        _id, vacancy_id, task, fine = input().strip().split(',')
        arr.append((_id, vacancy_id, int(task), int(fine)))

    return vacancy, arr

vacancy, arr = read_input()
for player in get_player(vacancy, arr):
    print(player)
