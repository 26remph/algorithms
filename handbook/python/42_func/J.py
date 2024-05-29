def secret_replace(s, /, **kwargs):
    shift = {}
    ans = []
    for ch in s:
        keys = kwargs.get(ch)
        if keys:
            ind = shift.get(keys, 0)
            ans.append(keys[ind])
            shift[keys] = (ind + 1) % len(keys)
        else:
            ans.append(ch)

    return ''.join(map(str, ans))


if __name__ == '__main__':
    result = secret_replace("Hello, world!", l=("hi", "y"), o=("123", "z"))
    print(result)
    result = secret_replace(
        "ABRA-KADABRA",
        A=("Z", "1", "!"),
        B=("3",),
        R=("X", "7"),
        K=("G", "H"),
        D=("0", "2"),
    )