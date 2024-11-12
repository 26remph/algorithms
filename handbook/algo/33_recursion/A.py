n = int(input())


# cnt = [0]
def dfs(n, from_, to_):
    # cnt[0] += 1

    if n == 1:
        print(from_, to_)
        return

    unused = 6 - from_ - to_
    dfs(n - 1, from_, unused)
    print(from_, to_)
    dfs(n - 1, unused, to_)


print(pow(2, n) - 1)
dfs(n, 1, 3)
# print(cnt)
