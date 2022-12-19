t = 1.0
print(id(t+t), id(t*2))

ans = (t+t) is (t*2)
print(ans)