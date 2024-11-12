from typing import List, Tuple


# import time


def foo(vacancy: dict, arr: List[Tuple[str, str, int, int]]) -> List[str]:
    staff: List[str] = []
    vacancy_sorted = dict(sorted(vacancy.items(), key=lambda x: x[0]))
    arr.sort(key=lambda x: (x[1], -x[2], x[3]))

    for name, capacity in vacancy_sorted.items():
        count: int = 0

        if not arr:
            break

        # names: list = []
        while count < len(arr) and arr[count][1] == name:
            if count < capacity:
                # names.append(arr[count][0])
                staff.append(arr[count][0])
            count += 1

        # staff = staff + names
        del arr[:count]

    staff.sort()

    return staff


def read_input() -> Tuple[dict, list]:
    n = int(input())
    vacancy = {}
    for _ in range(n):
        name, capcity = input().strip().split(",")
        vacancy[name] = int(capcity)
    k: int = int(input())
    arr = []
    for _ in range(k):
        candidate_id, vacancy_id, task, fine = input().strip().split(",")
        arr.append((candidate_id, vacancy_id, int(task), int(fine)))

    return vacancy, arr


# if __name__ == '__main__':
vacancy, arr = read_input()
# start_time = time.time()
for staff in foo(vacancy, arr):
    print(staff)
# print("--- %s seconds ---" % (time.time() - start_time))
