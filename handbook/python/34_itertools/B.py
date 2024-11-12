lst1 = input().split(", ")
lst2 = input().split(", ")
for pair in zip(lst1, lst2, strict=False):
    print(f"{pair[0]} - {pair[1]}")
