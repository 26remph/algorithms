def make_list(length, value=0):
    return [value for _ in range(length)]


if __name__ == '__main__':
    print(make_list(3))
    print(make_list(5, 1))
