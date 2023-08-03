name = input()
n = int(input())

path = []
for i in range(n):
    row = input()
    file = row.strip()
    cnt = sum([1 for ch in row if ch == ' '])
    path = path[:cnt]
    path.append(file)
    if file == name:
        print('/' + '/'.join(path))
        break
