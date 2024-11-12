arr = input().strip("/").split("/")

# print(arr)

ans = []
for i in range(len(arr)):
    if arr[i] == "" or arr[i] == ".":
        continue
    elif arr[i] == "..":  # > ....
        if len(ans) > 0:
            ans.pop()
    else:
        ans.append(arr[i])

# print(ans)
print("/" + "/".join(ans))
