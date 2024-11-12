v1, v2, v3 = int(input()), int(input()), int(input())
if v1 > v2 > v3:
    print("1. Петя")
    print("2. Вася")
    print("3. Толя")
elif v1 > v3 > v2:
    print("1. Петя")
    print("2. Толя")
    print("3. Вася")
elif v2 > v1 > v2:
    print("1. Вася")
    print("2. Петя")
    print("3. Толя")
elif v2 > v3 > v1:
    print("1. Вася")
    print("2. Толя")
    print("3. Петя")
elif v3 > v1 > v2:
    print("1. Толя")
    print("2. Петя")
    print("3. Вася")
elif v3 > v2 > v1:
    print("1. Толя")
    print("2. Вася")
    print("3. Петя")
