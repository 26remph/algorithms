n = int(input())
t1 = list(map(int, input().split(" ")))[::-1]

t2 = []
last = 0
isBroken = False
while t1:
    if t2 and last + 1 == t2[-1]:
        last = t2.pop()
    else:
        if last + 1 == t1[-1]:
            last = t1.pop()
        else:
            t2.append(t1.pop())

while t2:
    if last + 1 == t2[-1]:
        last = t2.pop()
    else:
        isBroken = True
        break

print("YES" if not isBroken else "NO")
