def fib(n):
    a, b = 0, 1
    for i in range(n):
        yield b
        a, b = b, a + b

    return b


if __name__ == "__main__":
    print(list(fib(10)))
