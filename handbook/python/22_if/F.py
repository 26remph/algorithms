year = int(input())

YES = "YES"
NO = "NO"

if year % 400 == 0:
    print(YES)
elif year % 100 == 0:
    print(NO)
elif year % 4 == 0 and year >= 8:
    print(YES)
else:
    print(NO)
