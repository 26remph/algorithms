odd_sum: float = 0
even_sum: float = 0
even_avg: float = 0
odd_avg: float = 0
odd_cnt, even_cnt = 0, 0


def enter_results(*args: float):
    global odd_sum, even_sum, odd_avg, even_avg, even_cnt, odd_cnt
    for i in range(len(args)):
        if i % 2 == 0:
            odd_sum += args[i]
            odd_cnt += 1
        else:
            even_sum += args[i]
            even_cnt += 1

    if odd_cnt:
        odd_avg = round(odd_sum / odd_cnt, 2)

    if even_cnt:
        even_avg = round(even_sum / even_cnt, 2)


def get_sum():
    return odd_sum, even_sum


def get_average():
    return odd_avg, even_avg


if __name__ == '__main__':
    # test 1
    # print('test1')
    # enter_results(1, 2, 3, 4, 5, 6)
    # print(get_sum(), get_average())
    # enter_results(1, 2)
    # print(get_sum(), get_average())
    # test 2
    print('test2')
    enter_results(3.5, 2.14, 45.2, 37.99)
    print(get_sum(), get_average())
    enter_results(5.2, 7.3)
    print(get_sum(), get_average())
    enter_results(1.23, 4.56, 3.14, 2.71, 0, 0)
    print(get_sum(), get_average())
