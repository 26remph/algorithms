eat = ["Манная", "Гречневая", "Пшённая", "Овсяная", "Рисовая"]
N = int(input())
if len(eat) >= N:
    print("\n".join(eat[:N]))
elif len(eat) < N:
    full = N // len(eat)
    tall = N - full * len(eat)
    for _ in range(full):
        print("\n".join(eat))
    print("\n".join(eat[:tall]))
