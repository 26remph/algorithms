def check(cost):

    var1 = (cost // c2 + cost % c2 // c5 * 4) + n >= m
    var2 = (cost // c5 * 4 + cost % c5 // c2) + n >= m
    # col1 = (cost // c2 + cost % c2 // c5 * 4)
    # col2 = (cost // c5 * 4 + cost % c5 // c2)
    # print(f'{var1=}, {var2=}, {col1=}, {col2=}, {cost=}')
    return var1 or var2


def bin_search(l, r):

    while l < r:
        cost = (l + r) // 2
        if check(cost):
            r = cost
        else:
            l = cost + 1

    return l


if __name__ == '__main__':
    n = int(input())
    m = int(input())
    c2 = int(input())
    c5 = int(input())
    print(bin_search(0, m * c2 + m * c5))

    # test = (
    #     (1, 3, 1, 10, 2),
    #     (2, 4, 9, 10, 10),
    #     (3, 8, 9, 10, 19),
    #     (3, 1, 1, 5, 0)
    # )
    # for n, m, c2, c5, ans in test:
    #     res = bin_search(0, m * c2 + m * c5)
    #     assert res == ans, f'{n=}, {m=}, {c2=}, {c5=}, {ans=}, {res=}'
