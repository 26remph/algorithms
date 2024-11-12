import math


def main():
    n = int(input())
    ans = [math.prod(map(int, input().split())) for _ in range(n)]
    print("\n".join([f"{(ans[i] / sum(ans)):.12f}" for i in range(len(ans))]))


if __name__ == "__main__":
    main()
