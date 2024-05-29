ans = set()
while s := input():
    arr = s.split()
    for i in range(len(arr)):
        if arr[i] == 'зайка' and i > 0:
            ans.add(arr[i - 1])

        if arr[i] == 'зайка' and i < len(arr) - 1:
            ans.add(arr[i + 1])

print('\n'.join(ans))
