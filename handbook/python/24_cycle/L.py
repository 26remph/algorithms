def solution(n, m):
    num = 1
    frmt = str(len(str(n * m))) + "d"
    for i in range(1, n + 1):
        arr = [f"{j:{frmt}}" for j in range(num, num + m)]
        num += len(arr)
        print(" ".join(arr))


if __name__ == "__main__":
    n, m = int(input()), int(input())
    solution(n, m)
