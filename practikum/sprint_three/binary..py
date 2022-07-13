def get_binary(n, prefix):
    if n == 0:
        print(prefix)
    else:
        get_binary(n - 1, prefix + '0')
        get_binary(n - 1, prefix + '1')


get_binary(8, '')