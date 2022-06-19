from typing import List, Tuple, Dict
import time


def judge(x, name, cnt):
    if x[1] == name:
        cnt['count'] += 1
        return True

    return False


def foo(vacancy: dict, arr: List[Tuple[str, str, int, int]]) -> List[str]:

    staff: List[str] = []
    vacancy_sorted = dict(sorted(vacancy.items(), key=lambda x: x[0]))
    arr.sort(key=lambda x: (x[1], -x[2], x[3]))

    # print(vacancy_sorted)
    # print(arr)
    # return staff

    for name, capacity in vacancy_sorted.items():
        count: int = 0
        # filtered_vacancy = list(filter(lambda x: x[1] == name, arr))
        # rez: list = sorted(filtered_vacancy, key=lambda x: (-x[2], x[3]))
        # filtered_vacancy = list(filter(lambda x: x[1] == name, arr))
        # arr.sort(key=lambda x: (-judge(x, name, cnt), -x[2], x[3]))
        # print('arr:', arr)
        # print('count', cnt)
        if not arr:
            break

        names: list = []
        while count < len(arr) and arr[count][1] == name:
            # print('arr[count]', arr[count])
            # print('count', count)
            if count < capacity:
                names.append(arr[count][0])

            count += 1

        # end_names: int = min(count, capacity)
        # end_slice: int = count

        # print('arr end:', arr[:end])
        # names = [x[0] for x in arr[:end_names]]
        staff = staff + names
        # print('names:', names)
        del arr[:count]
        # return staff

        # end: int = min(len(rez), capcity)
        # names = [x[0] for x in rez[:end]]
        # staff = staff + names

    staff.sort()

    return staff


def read_input() -> Tuple[dict, list]:
    # file input
    with open('inp_vaconcy_all.txt') as f:
        n = int(f.readline())
        vacancy = {}
        for _ in range(n):
            name, capcity = f.readline().strip().split(',')
            vacancy[name] = int(capcity)
        k: int = int(f.readline())
        arr = []
        for _ in range(k):
            candidate_id, vacancy_id, task, fine = f.readline().split(',')
            arr.append((candidate_id, vacancy_id, int(task), int(fine)))

    # stdin input
    # n = int(input())
    # vacancy = {}
    # for _ in range(n):
    #     name, capcity = input().strip().split(',')
    #     vacancy[name] = int(capcity)
    # k: int = int(input())
    # arr = []
    # for _ in range(k):
    #     candidate_id, vacancy_id, task, fine = input().strip().split(',')
    #     arr.append((candidate_id, vacancy_id, int(task), int(fine)))

    return vacancy, arr


if __name__ == '__main__':
    vacancy, arr = read_input()
    start_time = time.time()
    for staff in foo(vacancy, arr):
        print(staff)
    # print('\n'.join(foo(vacancy, arr)))
    print("--- %s seconds ---" % (time.time() - start_time))
