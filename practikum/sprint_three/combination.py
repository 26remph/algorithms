TOUCH = {
    2: 'abc',
    3: 'def',
    4: 'ghi',
    5: 'jkl',
    6: 'mno',
    7: 'pqrs',
    8: 'tuv',
    9: 'wxyz'
}

COMBOS = []


def get_combo(start, indent = 0, prefix = ''):

    if start == 0:
        # print(prefix)
        COMBOS.append(prefix)
    else:
        for i in range(len(press[indent+1])):
            get_combo(start - 1, indent + 1, prefix + press[indent+1][i])


keys = [int(x) for x in input()]
press = [TOUCH[x] for x in keys]
# print(press)

cnt = len(press) - 1
for x in press[0]:
    get_combo(cnt, prefix=x)

print(*COMBOS)

