def make_linear(arr, res=None):
    if res is None:
        res = []

    for elem in arr:
        if isinstance(elem, list):
            make_linear(elem, res)
        else:
            res.append(elem)

    return res

input_arr = [1, [2, [3, 4]], 5, 6]
result = make_linear(input_arr)
print(result)