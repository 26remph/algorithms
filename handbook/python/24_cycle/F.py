def gcd(a, b):
    while b > 0:
        a %= b
        a, b = max(a, b), min(a, b)
        print(a, b)

    return a


def solution(arr):
    arr.sort(reverse=True)
    tail = arr[-1]
    while tail > 0:
        for i in range(len(arr) - 1):
            arr[i] = arr[i] % tail

        arr.sort(reverse=True)

        while arr and not arr[-1]:
            arr.pop()

        if len(arr) == 1:
            return tail

        tail = arr[-1]

    return tail


if __name__ == "__main__":
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(int(input()))

    print(solution(arr))
    # print(gcd(17, 13))
