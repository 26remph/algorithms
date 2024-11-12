import collections


if __name__ == "__main__":
    n, k = map(int, input().split())
    pr = [0]
    pr += list(map(int, input().split()))
    lst = []
    d = collections.defaultdict(list)
    for i in range(n):
        r, _, *desire = list(map(int, input().split()))
        d[i] = desire
        lst.append((i, r))

    lst.sort(key=lambda x: x[1])
    ans = []
    for i, _ in lst:
        flag = False
        for p in d[i]:
            if pr[p] > 0:
                pr[p] -= 1
                ans.append((i, p))
                flag = True
                break

        if not flag:
            ans.append((i, -1))

    # print(d)
    # print(f'{lst=}, {pr=}')

    ans.sort(key=lambda x: x[0])
    # print(f'{ans=}')
    print(" ".join(map(str, [r for i, r in ans])))
