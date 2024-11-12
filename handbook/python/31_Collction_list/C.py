L = int(input())
N = int(input())
for _ in range(N):
    s = input()
    if len(s) > L:
        print(s[: L - 3] + "...")
    else:
        print(s)
