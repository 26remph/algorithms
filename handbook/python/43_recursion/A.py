result = 0


def recursive_sum_for(*args):
    global result

    if len(args) == 1:
        return args[0]

    for arg in args:
        result += recursive_sum_for(arg)

    return result


def recursive_sum(*args):
    global result

    if len(args):
        result += list(args).pop()
        recursive_sum(*args[:-1])

    return result


if __name__ == '__main__':
    print(recursive_sum(1, 2, 3))