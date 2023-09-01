L = int(input())
N = int(input())
for _ in range(N):
    s = input()
    if L < len(s):
        print(s[:L-3] + '...')
    else:
        print(s)

