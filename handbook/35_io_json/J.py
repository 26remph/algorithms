fn = input()
n = int(input())

with open(fn, encoding="UTF-8") as f:
    while True:
        s = f.readline()
        if not s:
            break