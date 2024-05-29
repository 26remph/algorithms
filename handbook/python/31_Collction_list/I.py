while s := input():
    ind = s.find('#')
    if ind == -1:
        print(s)
    elif ind == 0:
        continue
    else:
        print(s[:ind])

