d = int(input())
X, Y = map(int, input().split())

if X >= 0 and Y >= 0 and X + Y <= d:
    print(0)
else:
    A_dist = pow(pow(abs(X), 2) + pow(abs(Y), 2), 0.5)
    B_dist = pow((pow(abs(X - d), 2) + pow(abs(Y), 2)), 0.5)
    C_dist = pow(pow(abs(Y-d), 2) + pow(X, 2), 0.5)

    ans = min(enumerate([A_dist, B_dist, C_dist]), key=lambda x: x[1])
    print('A_dist', A_dist)
    print('B_dist', B_dist),
    print('C_dist', C_dist)

    print(ans)
    print(ans[0] + 1)

