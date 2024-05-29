from collections import defaultdict


def result_accumulator(func):

    queue = defaultdict(list)

    def warp(*args, method='accumulate'):

        queue[id(func)].append(func(*args))

        if method == 'drop':
            dump = queue[id(func)][:]
            queue[id(func)].clear()
            return dump

    return warp


@result_accumulator
def a_plus_b(a, b):
    return a + b


@result_accumulator
def get_letters(text: str) -> str:
    return ''.join(sorted(set(filter(str.isalpha, text.lower()))))


if __name__ == '__main__':
    # test 1
    print(a_plus_b(3, 5, method="accumulate"))
    print(a_plus_b(7, 9))
    print(a_plus_b(-3, 5, method="drop"))
    print(a_plus_b(1, -7))
    print(a_plus_b(10, 35, method="drop"))
    # test 2
    print()
    print(get_letters('Hello, world!'))
    print(get_letters('Декораторы это круто =)'))
    print(get_letters('Ехали медведи на велосипеде', method='drop'))
