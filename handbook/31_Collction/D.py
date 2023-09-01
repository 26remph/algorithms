prefix = '##'
suffix = '@@@'

while s := input():

    if s.endswith(suffix):
        continue
    elif s.startswith(prefix):
        s = s[2:]
        if s:
            print(s)
    else:
        print(s)