# arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# print(arr[0:4])


def foo(arr):

    global arr
    arr = [1, 2]

    return arr


def test_():
    x = [6, 7, 8, 4, 5, 6]
    foo(x)
    print(x)

test_()
