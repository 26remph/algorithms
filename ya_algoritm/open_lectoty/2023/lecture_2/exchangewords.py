key = set(input().split())
arr = input().split()
out = []
for i in range(len(arr)):
    s = arr[i]
    prefix = ''
    ans = s
    for j in range(len(s)):
        prefix = ''.join([prefix, s[j]])
        if prefix in key:
            ans = prefix
            break

    out.append(ans)

print(' '.join(out))
