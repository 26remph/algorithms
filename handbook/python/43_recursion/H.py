def fibonacci(n):
    if n == 0:
        yield
    elif n == 1:
        yield 0
    else:
        a, b = 0, 1
        yield a
        yield b
        for _ in range(n - 2):
            a, b = b, a + b
            yield b


print(*fibonacci(0), sep=", ")
print(*fibonacci(1), sep=", ")
print(*fibonacci(2), sep=", ")
print(*fibonacci(5))
