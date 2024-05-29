# s = input()

cnt = 0
for dig in range(100, 999):

    s = str(dig)

    sum_dig = int(s[0]) + int(s[1]) + int(s[2])
    max_val = int(max(s))
    min_val = int(min(s))
    last = sum_dig - max_val - min_val

    if last * 2 == max_val + min_val:
        cnt += 1
        print('nice dig: ', dig)

print(cnt)
