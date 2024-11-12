def to_string(*args, sep=" ", end="\n") -> str:
    return sep.join(map(str, args)) + end


if __name__ == "__main__":
    print(to_string(1, 2, 3))
    data = [7, 3, 1, "hello", (1, 2, 3)]
    print(to_string(*data, sep=", ", end="!"))
