n = int(input())

if n == 0 or n == 1:
    print("NO")
else:
    flag = False
    for i in range(2, n):
        if n % i == 0:
            print("NO")
            flag = True
            break

    if not flag:
        print("YES")
