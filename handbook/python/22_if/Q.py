a, b, c = float(input()), float(input()), float(input())

if a == b == c == 0:
    print("Infinite solutions")
elif a != 0:
    D = pow(b, 2) - 4 * a * c
    if D > 0:
        x1 = (-b + pow(D, 0.5)) / (2 * a)
        x2 = (-b - pow(D, 0.5)) / (2 * a)
        print(f"{min(x1, x2):0.2f} {max(x1, x2):0.2f}")
    elif D == 0:
        x1 = -b / (2 * a)
        print(f"{x1:0.2f}")
    else:
        print("No solution")
elif a == 0 and b != 0:
    x1 = -c / b
    print(f"{x1:0.2f}")
else:
    print("No solution")
