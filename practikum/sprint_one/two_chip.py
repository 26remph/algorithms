from typing import List, Optional, Tuple


def two_sum(arr: List[int], target_sum: int) -> Optional[Tuple[int, int]]:
    arr_diff: list = []
    for num in arr:
        arr_diff.append((num - target_sum) * -1)

    pairs = list(set(arr).intersection(arr_diff))

    if len(pairs) == 1:
        return (pairs[0], pairs[0]) if arr.count(pairs[0]) > 1 else None

    for num in pairs:
        pair_num = num * -1 + target_sum
        if pair_num == num:
            if arr.count(num) > 1:
                return num, num
            else:
                continue

        if pair_num in pairs:
            return num, pair_num

    return None


def read_input() -> Tuple[List[int], int]:
    n = int(input())
    arr = list(map(int, input().strip().split()))
    target_sum = int(input())
    return arr, target_sum


def print_result(result: Optional[Tuple[int, int]]) -> None:
    if result is None:
        print(None)
    else:
        print(" ".join(map(str, result)))


arr, target_sum = read_input()
print_result(two_sum(arr, target_sum))
