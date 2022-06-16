j = input().strip()
s = input().strip()

result = 0
for ch in s:
    if ch in j:
        result += 1

print(result)
