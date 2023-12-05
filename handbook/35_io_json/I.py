f1 = open(input(), encoding='UTF-8')
f2 = open(input(), 'w', encoding='UTF-8')

ans = []
for line in f1:

    wrds = []
    wrd = ""
    for ch in line:
        if ch == "\t":
            continue

        if ch != " ":
            wrd += ch
        else:
            if wrd:
                wrds.append(wrd)
            wrd = ""

    wrds.append(wrd)
    if len(wrds) == 1 and wrds[0] == "\n":
        continue

    f2.write(' '.join(wrds))


f1.close()
f2.close()
