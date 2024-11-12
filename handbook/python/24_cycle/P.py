def solution(n, width):
    for i in range(1, n + 1):
        end = "|"
        for j in range(1, n + 1):
            if j == n:
                end = "\n"
            print(f"{i * j:^{width}d}", end=end)

        if i != n:
            print("-" * (width * n + n - 1))


if __name__ == "__main__":
    n, m = int(input()), int(input())
    solution(n, m)
