numbers = [1, 1, 3, 1, 10, 2, 4, 6, 7, 1, 2, 7]
ans = ' - '.join([str(x) for x in sorted(list(set(numbers)))])
print(ans)
