def solution(n):
    lvl = 1
    i = 1
    while i < n + 1:
        ans = []
        for j in range(i, min(i + lvl, n + 1)):
            ans.append(str(j))
        print(" ".join(ans))

        i = i + lvl
        lvl += 1


if __name__ == "__main__":
    n = int(input())
    solution(n)
