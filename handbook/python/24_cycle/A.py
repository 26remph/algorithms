def solution():
    for i in range(1, n + 1):
        ans = []
        for j in range(1, n + 1):
            ans.append(str(i * j))
        print(" ".join(ans))


if __name__ == "__main__":
    n = int(input())
    solution()
