from collections import Counter


def main():
    _ = int(input())
    arr = list(map(int, input().split()))
    cnt = Counter(arr)

    arr = cnt.most_common()
    col = arr[0][1]
    ind = 0
    ans = arr[0][0]

    while ind < len(arr) and arr[ind][1] == col:
        ans = max(arr[ind][0], ans)
        ind += 1

    print(ans)


if __name__ == '__main__':
    main()