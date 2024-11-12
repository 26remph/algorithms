from typing import Optional


def ext_list(s: str, arr: Optional[list] = None) -> list:
    if arr is None:
        arr = []
    arr.append(s)
    return arr


val = "zero"
inp_arr = ["1", "2", "3"]
print(ext_list(val, inp_arr))
print(ext_list(val))
print(ext_list(val))
