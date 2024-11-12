if __name__ == "__main__":
    n = int(input())
    ax = list(map(int, input().split()))
    m = int(input())
    bx = list(map(int, input().split()))

    size = max(n, m)
    print(size)
    ax = [0] * (size - n) + ax
    bx = [0] * (size - m) + bx
    for a, b in zip(ax, bx, strict=False):
        print(a + b, end=" ")
