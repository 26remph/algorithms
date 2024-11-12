S = input()
pref = [0] * (len(S) + 1)

flag = True
for i in range(len(S)):
    cur = 1 if S[i] == "(" else -1
    pref[i + 1] = pref[i] + cur
    if pref[i + 1] < 0:
        flag = False
        break

# print(pref)
if flag:
    print("YES" if pref[-1] == 0 else "NO")
else:
    print("NO")
