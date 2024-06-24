def count(func):

    count = 0

    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        return func(*args, *kwargs), count

    return wrapper


@count
def hello(n):
    return f'Hello {n}'


if __name__ == '__main__':
    print(hello('Maksim'))
    print(hello('Maksim'))
    print(hello('Maksim'))
    print(hello('Maksim'))
