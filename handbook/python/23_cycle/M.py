N = input()

_min = ''
for _ in range(int(N)):
    name = input()
    if not _min or name < _min:
        _min = name

print(_min)
