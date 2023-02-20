s = input()

i, k = 0, len(s) - 1

ans = 'YES'
while i < k:
    if s[i] != s[k]:
        ans = 'NO'
        break

    i += 1
    k -= 1

print(ans)
