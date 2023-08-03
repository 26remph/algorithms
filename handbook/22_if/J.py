num = int(input())
a, b, c = str(num)
if int(a) + int(b) > int(b) + int(c):
    num = str(int(a) + int(b)) + str(int(b) + int(c))
else:
    num = str(int(b) + int(c)) + str(int(a) + int(b))

print(num)