from itertools import product


S = int(input())
A = list(map(int, input().split()))[1:]
B = list(map(int, input().split()))[1:]
C = list(map(int, input().split()))[1:]

setC = set(C)

AB = product(range(len(A)), range(len(B)))

indAC = []

for i, j in AB:
    if S - A[i] - B[j] in setC:
        indAC.append((i, j))
        break
if indAC:
    ind_a, ind_b = indAC[0]
    c = S - A[ind_a] - B[ind_b]
    ind_c = C.index(c)
    print(ind_a, ind_b, ind_c)
else:
    print(-1)
