N, M = int(input()), int(input())

manka = {input() for _ in range(N)}
oves = {input() for _ in range(M)}

ans = manka & oves
if ans:
    print(len(ans))
else:
    print("Таких нет")
