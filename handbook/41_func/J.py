from random import randint


def merge(a1: tuple, a2: tuple) -> tuple:
    ans = []
    i, j = 0, 0
    while i < len(a1) and j < len(a2):
        if a1[i] < a2[j]:
            ans.append(a1[i])
            i += 1
        elif a1[i] > a2[j]:
            ans.append(a2[j])
            j += 1
        else:
            ans.append(a1[i])
            ans.append(a2[j])
            i += 1
            j += 1

    if i < len(a1):
        ans.extend(a1[i:])

    if j < len(a2):
        ans.extend(a2[j:])

    return tuple(ans)


if __name__ == '__main__':
    # print(merge((1, 2), (3, 4, 5)))
    # print(merge((7, 12), (1, 9, 50)))
    for _ in range(10_000):
        a1 = [randint(1, 10) for _ in range(randint(1, 10))]
        a2 = [randint(1, 10) for _ in range(randint(1, 10))]
        a1.sort()
        a2.sort()
        arr = a1 + a2
        arr.sort()
        assert merge(tuple(a1), tuple(a2))== tuple(arr), f'{a1=}, {a2=}, {arr=}'
