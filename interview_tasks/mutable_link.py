def f(sum, l=[]):
    l.append(sum)
    print(id(l), l)


df = f.__defaults__
l = [1]

print(df)
print(df[0], id(df[0]))
f(10)  # [10]
print(df[0], id(df[0]))

f(10)  # [10, 10]
print(df)
print(df[0], id(df[0]))

f(10, l)  # [1, 10]
print(df)
print(df[0], id(df[0]))

# f(10)       # [10, 10, 10]
# print(id(l), l)    # [1, 10]
