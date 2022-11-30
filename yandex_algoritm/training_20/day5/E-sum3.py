from itertools import starmap, product
import random

# S = random.randint(1, 200)
# A = [random.randint(1, 100) for _ in range(1, 20)]
# B = [random.randint(1, 100) for _ in range(1, 20)]
# C = [random.randint(1, 100) for _ in range(1, 20)]

# S = 96
# A = [59, 36, 86, 14, 5, 6, 96, 78, 21, 42, 93, 46, 40, 16, 50, 47, 22, 62, 82]
# B = [51, 60, 71, 14, 48, 22, 89, 88, 68, 61, 43, 53, 96, 87, 47, 87, 19, 63, 15]
# C = [72, 29, 23, 48, 4, 58, 37, 87, 13, 2, 35, 28, 76, 12, 36, 87, 25, 21, 4]
# print(S)
# print(A)
# print(B)
# print(C)

# S = int(input())
# A = list(map(int, input().split()))[1:]
# B = list(map(int, input().split()))[1:]
# C = list(map(int, input().split()))[1:]

def short_foo():
    setC = set(C)

    AB = product(range(len(A)), range(len(B)))

    indAC = []

    # for i in range(len(A)):
    #     for j in range(len(B)):
    #         if S - A[i] - B[j] in setC:
    #             indAC.append((i, j))
    for i, j in AB:
        print(i, j)
        if S - A[i] - B[j] in setC:
            indAC.append((i, j))
            break

    if indAC:
        # indAC.sort()
        # print('indAC', indAC)
        ind_a, ind_b = indAC[0]
        c = S - A[ind_a] - B[ind_b]
        ind_c = C.index(c)
        # print('short', ind_a, ind_b, ind_c)
        return ind_a, ind_b, ind_c
    else:
        # print(-1)
        return -1


def long_foo():
    BC = product(B, C)
    sumBC_gen = starmap(lambda x, y: x + y, BC)

    B_plus_C = set(sumBC_gen)


    ind_a = len(A)
    for ind in range(len(A)):
        if (S - A[ind]) in B_plus_C:
            ind_a = min(ind_a, ind)

    del B_plus_C

    ans = []
    if ind_a == len(A):
        # print(-1)
        return -1
    else:
        BC = product(B, C)
        for pair in BC:
            if S - A[ind_a] == pair[0] + pair[1]:
                ind_b = B.index(pair[0])
                ind_c = C.index(pair[1])
                ans.append((ind_b, ind_c))

        ans.sort()
        ind_b, ind_c = ans[0]
        # print('long', ind_a, ind_b, ind_c)
        return ind_a, ind_b, ind_c


PASS = 1000
while PASS:
    S = random.randint(1, 200)
    A = [random.randint(1, 100) for _ in range(1, 20)]
    B = [random.randint(1, 100) for _ in range(1, 20)]
    C = [random.randint(1, 100) for _ in range(1, 20)]
    assert short_foo() == long_foo(), f'{S}\n{A}\n{B}\n{C}'
    PASS -= 1