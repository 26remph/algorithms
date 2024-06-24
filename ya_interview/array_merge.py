def solution(a1: list, a2: list) -> list:

    out = []
    while a1 and a2:
        if a1[-1] > a2[-1]:
            num = a1.pop()
            if out and num != out[-1] or not out:
                out.append(num)

        elif a1[-1] < a2[-1]:
            num = a2.pop()
            if out and num != out[-1] or not out:
                out.append(num)
        else:
            a1.pop()
            num = a2.pop()
            if out and num != out[-1] or not out:
                out.append(num)

    for num in reversed(a1):
        if out and num != out[-1] or not out:
            out.append(num)

    for num in reversed(a2):
        if out and num != out[-1] or not out:
            out.append(num)

    return out[::-1]


if __name__ == '__main__':
    tests = [
        ([1, 2, 3, 4], [0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5]),
        ([1, 1, 2, 2], [3], [1, 2, 3]),
        ([1], [2], [1, 2]),
        ([], [1], [1]),
        ([1], [], [1]),
        ([1, 1], [2, 2], [1, 2]),
        ([], [], []),
    ]

    for arr1, arr2, ans in tests:
        res = solution(arr1, arr2)
        assert res == ans, f'{res=}, {ans=}'