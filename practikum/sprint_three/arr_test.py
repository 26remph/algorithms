# arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# print(arr[0:4])


def foo(arr):
    arr[0] = 1
    arr[1] = 1
    arr[2] = 1
    return arr

def test():
    x = [6, 7, 8, 4, 5, 6]
    print(x)
    foo(x)
    print(x)

if __name__ == '__main__':
    test()
