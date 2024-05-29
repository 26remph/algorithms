a = int(input().split('=')[1])
b = int(input().split('=')[1])
print([pow(x, 2) for x in range(a, b + 1)])
