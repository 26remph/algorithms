letters = [0] * ord("я")

while (s := input()) != "ФИНИШ":
    for ch in s.lower():
        if ch == " ":
            continue
        letters[ord(ch)] += 1

max_ = 0
ans = ""
for i in range(len(letters)):
    if letters[i] > max_:
        ans = chr(i)
        max_ = letters[i]
print(ans)
