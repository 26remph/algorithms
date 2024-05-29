arr = list(map(bin, map(int, input().split())))
ans = []
for num in arr:
    num = num[2:]
    d = {
        "digits": len(num),
        "units": len([x for x in str(num) if x == '1']),
        "zeros": len([x for x in str(num) if x == '0'])
    }
    ans.append(d)

print(ans)

