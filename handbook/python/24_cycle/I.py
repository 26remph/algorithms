if __name__ == "__main__":
    N = int(input())
    ans = []
    for _ in range(N):
        max_num = max(map(int, list(input())))
        ans.append(max_num)

    print("".join(map(str, ans)))
