def dfs(n, from_rod, to_rod, ext1, ext2):

    if n == 0:
        return

    if n == 1:
        # print(from_rod, to_rod)
        cnt[0] += 1
        return

    dfs(n - 2, from_rod, ext1, ext2, to_rod)
    # print(from_rod, ext2)
    # print(from_rod, to_rod)
    # print(ext2, to_rod)
    cnt[0] += 3

    dfs(n - 2, ext1, to_rod, from_rod, ext2)


if __name__ == '__main__':
    n = int(input())
    cnt = [0]
    dfs(n, 1, 4, 2, 3)
    print(cnt[0])