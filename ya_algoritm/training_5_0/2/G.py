def solution(a):
    cut_l = 1
    cur_min = a[0]
    res = []
    for i in range(len(a)):
        if cur_min > a[i]:
            cur_min = a[i]

        if cur_min < cut_l:
            res.append(cut_l - 1)
            cut_l = 1
            cur_min = a[i]

        cut_l += 1

    res.append(cut_l - 1)
    return len(res), res


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        _ = input()
        arr = list(map(int, input().split()))
        ans = solution(arr)
        print(f'{ans[0]}\n{" ".join(map(str, ans[1]))}')
