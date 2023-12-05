from sys import stdin

lst = []
for row in stdin:
    lst.append(row.rstrip())

query = lst.pop()
for header in lst:
    pos = header.lower().find(query.lower())
    if pos > -1:
        print(header)

