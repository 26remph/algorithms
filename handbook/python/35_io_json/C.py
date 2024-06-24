from sys import stdin


for row in stdin:
    pos = row.find("#")
    if pos > 0:
        print(row[:pos].rstrip())
    elif pos == -1:
        print(row.rstrip())
