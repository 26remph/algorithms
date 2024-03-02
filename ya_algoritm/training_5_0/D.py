
def rock_handler(i, j):
    # right
    for aj in range(j + 1, 8):
        if arr[i][aj] == 'B' or arr[i][aj] == 'R':
            break
        arr[i][aj] = 'X'

    # left
    for aj in range(j - 1, -1, -1):
        if arr[i][aj] == 'B' or arr[i][aj] == 'R':
            break
        arr[i][aj] = 'X'

    # down
    for ai in range(i + 1, 8):
        if arr[ai][j] == 'B' or arr[ai][j] == 'R':
            break
        arr[ai][j] = 'X'

    # up
    for ai in range(i - 1, -1, -1):
        if arr[ai][j] == 'B' or arr[ai][j] == 'R':
            break
        arr[ai][j] = 'X'


def bishop_handler(i, j):
    # up right
    ai, aj = i + 1, j - 1
    while ai < 8 and aj > -1:
        if arr[ai][aj] == 'B' or arr[ai][aj] == 'R':
            break
        arr[ai][aj] = 'X'
        ai += 1
        aj -= 1

    # down left
    ai, aj = i - 1, j + 1
    while ai > -1 and aj < 8:
        if arr[ai][aj] == 'B' or arr[ai][aj] == 'R':
            break
        arr[ai][aj] = 'X'
        ai -= 1
        aj += 1

    # up left
    ai, aj = i - 1, j - 1
    while ai > -1 and aj > -1:
        if arr[ai][aj] == 'B' or arr[ai][aj] == 'R':
            break
        arr[ai][aj] = 'X'
        ai -= 1
        aj -= 1

    # down right
    ai, aj = i + 1, j + 1
    while ai < 8 and aj < 8:
        if arr[ai][aj] == 'B' or arr[ai][aj] == 'R':
            break
        arr[ai][aj] = 'X'
        ai += 1
        aj += 1


if __name__ == '__main__':
    arr = [[ch for ch in input().strip()] for _ in range(8)]
    for i in range(8):
        for j in range(8):
            if arr[i][j] == 'R':
                rock_handler(i, j)

            if arr[i][j] == 'B':
                bishop_handler(i, j)

    ans = 0
    for i in range(8):
        for j in range(8):
            ans += 1 if arr[i][j] == "*" else 0

    print(ans)
    # for i in range(8):
    #     print(arr[i])

