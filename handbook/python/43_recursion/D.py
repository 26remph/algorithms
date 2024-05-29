def answer(func):

    def warp(*args, **kwargs):
        return f'Результат функции: {func(*args, **kwargs)}'

    return warp

@answer
def a_plus(a, b):
    return a + b


if __name__ == '__main__':
    print(a_plus(3, 5))
    print(a_plus(7, 9))