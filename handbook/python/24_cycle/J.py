def solution(n):
    print("А Б В")
    for i in range(1, n - 1):
        for j in range(1, n - 1):
            if n - i - j > 0:
                print(i, j, n - i - j)


if __name__ == "__main__":
    N = int(input())
    solution(N)
