bases = list(map(int, input().split()))
p = int(input())
print(' '.join(map(str, map(lambda x: pow(x, p), bases))))
