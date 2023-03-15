import operator

s = input()

expr = s.split(' ')
stack = []

operand = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul
}

for ch in expr:
    func = operand.get(ch)
    if func:
        b = stack.pop()
        a = stack.pop()
        stack.append(func(a, b))
    else:
        stack.append(int(ch))

print(stack[0])