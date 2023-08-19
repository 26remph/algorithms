def solution(arr):

    flags = [0] * len(arr)
    for j in range(len(arr)):
        if flags[j] == 1:
            continue

        div = arr[j] * 2
        for i in range(len(arr)):
            if flags[i] == 1:
                continue

            if arr[i] == div:
                flags[i] = 1
                div *= 2

    # --
    ans = []
    for i in range(len(arr)):
        if flags[i] == 0:
            ans.append(arr[i])

    print(ans)


if __name__ == '__main__':
    n = int(input())
    arr = [x for x in range(2, n + 1)]
    solution(arr)
