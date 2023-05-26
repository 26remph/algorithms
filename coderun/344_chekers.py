def main():
    N, M = map(int, input().split())
    desk = [[0 for _ in range(M+1)] for _ in range(N+1)]

    w = int(input())
    w_set = set()
    for _ in range(w):
        i, j = map(int, input().split())
        desk[i][j] = 'W'
        w_set.add((i, j))

    b = int(input())
    b_set = set()
    for _ in range(b):
        i, j = map(int, input().split())
        desk[i][j] = 'B'
        b_set.add((i, j))

    move = input()

    for j in range(M+1):
        desk[0][j] = -1

    for i in range(N+1):
        desk[i][0] = -1
        print(desk[i])

    if move == 'white':
        player, opponent = w_set, b_set
    else:
        player, opponent = b_set, w_set

    occupy = w_set.union(b_set)
    env = [[(-1, -1), (-2, -2)], [(-1, 1), (-2, 2)], [(1, -1), (2, -2)],
           [(1, 1), (2, 2)]]

    for piece in player:

        for ind in range(len(env)):
            if (piece[0] + env[ind][0][0], piece[1] + env[ind][0][1]) in opponent:
                print('dot', env[ind])
                check_dot = piece[0] + env[ind][1][0], piece[1] + env[ind][1][1]
                print('check_dot', check_dot, N >= check_dot[0] > 0, M >= check_dot[1] > 0)
                if all([
                    N >= check_dot[0] > 0,
                    M >= check_dot[1] > 0,
                    check_dot not in occupy]):
                    print('Yes')
                    return

    print('No')

if __name__ == '__main__':
    main()
