DANGER = 'Опасность! Покиньте зону как можно скорее!'
FREE = 'Зона безопасна. Продолжайте работу.'
OUT = 'Вы вышли в море и рискуете быть съеденным акулой!'

x, y = float(input()), float(input())
R = 5
BIG_R = 10

if pow(x, 2) + pow(y, 2) > pow(BIG_R, 2):
    print(OUT)
elif x >= 0 and y >= 0:
    print(DANGER if pow(x, 2) + pow(y, 2) <= pow(R, 2) else FREE)
elif y <= 0:
    Fx = 0.25 * pow(x, 2) + 0.5 * x - 8.75
    print(DANGER if y >= Fx else FREE)
elif - 4 <= x < 0 < y <= 5:
    print(DANGER)
elif x < -4 < 0 < y <= 5:
    Fx = 1.6 * x + 11.2
    print(DANGER if y <= Fx else FREE)
else:
    print(FREE)
