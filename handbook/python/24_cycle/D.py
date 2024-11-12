def solution(s):
    col = 0
    for ch in s:
        col += int(ch)

    return col


if __name__ == "__main__":
    N = int(input())
    total = 0
    for _ in range(N):
        total += solution(input())

    print(total)
