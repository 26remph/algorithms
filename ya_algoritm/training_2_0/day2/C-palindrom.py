S = str(input())

L = len(S)
cost = 0
if (L == 2 or L == 3) and S[0] != S[-1]:
    cost = 1
else:
    for i in range(len(S) // 2):

        if S[i] != S[len(S) - 1 - i]:
            cost += 1


print(cost)
