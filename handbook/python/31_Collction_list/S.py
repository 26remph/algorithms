import math

from operator import add, floordiv, mul, sub


op = {
    "*": mul,
    "+": add,
    "-": sub,
    "/": floordiv,
    "~": lambda x: (-1) * x,
    "!": math.factorial,
    "#": lambda x: [x, x],
    "@": lambda x: (x.pop(), x.pop(), x.pop()),
}
bi = {"*", "+", "-", "/"}
uni = {"~", "!", "#"}
trio = {"@"}

arr = input().strip().split()
stack = []
for val in arr:
    func = op.get(val)
    if not func:
        stack.append(int(val))
    else:
        if val in bi:
            a = stack.pop()
            b = stack.pop()
            if val in "-/":
                a, b = b, a
            stack.append(func(a, b))
        elif val in uni:
            a = stack.pop()
            if val in "!~":
                stack.append(func(a))
            else:
                stack.extend(func(a))
        elif val in trio:
            a, b, c = func(stack)
            stack += [b, a, c]

    # print('s:', stack)
print("".join(map(str, stack)))
