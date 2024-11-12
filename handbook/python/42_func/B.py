def make_matrix(size, value=0):
    i, j = size, size
    if isinstance(size, tuple):
        i, j = size[0], size[1]
    return [[value for _ in range(i)] for _ in range(j)]


if __name__ == "__main__":
    print(make_matrix(3))
    print(make_matrix((4, 2), 1))
