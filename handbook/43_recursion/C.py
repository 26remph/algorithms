count = 0


def make_equation_forward(*args):
    global count
    if args:
        if not count:
            expr = ''.join(('(' for _ in range(len(args) - 1))) + f'{args[0]}'
        else:
            expr = f') * x + {args[0]}'

        count += 1

        return f'{expr}{make_equation(*args[1:])}'

    return ''


def make_equation(*num):
    if len(num) == 1:
        return f'{num[0]}'
    else:
        return f'({make_equation(*num[:-1])}) * x + {num[-1]}'


if __name__ == '__main__':
    count = 0
    print(make_equation(3))
    count = 0
    print(make_equation(3, 2))
    count = 0
    print(make_equation(3, 2, 1))
    count = 0
    print(make_equation(3, 1, 5, 3))
    count = 0
    print(make_equation(3, 1, 5, 3, 4))
