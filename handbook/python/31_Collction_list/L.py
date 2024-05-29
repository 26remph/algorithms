eat = ['Манная', 'Гречневая', 'Пшённая', 'Овсяная', 'Рисовая']
N = int(input())
if N <= len(eat):
    print('\n'.join(eat[:N]))
elif N > len(eat):
    full = N // len(eat)
    tall = N - full * len(eat)
    for _ in range(full):
        print('\n'.join(eat))
    print('\n'.join(eat[:tall]))
