x, y = 0, 0

while (s := input()) != 'СТОП':
    match s:
        case 'СЕВЕР':
            x += int(input())
        case 'ЮГ':
            x -= int(input())
        case 'ЗАПАД':
            y -= int(input())
        case 'ВОСТОК':
            y += int(input())
        case _:
            print('Not allowed way. Try again.')

print(f'{x}\n{y}')
