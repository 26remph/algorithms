N = int(input())
ingredients = set()
for _ in range(N):
    ingredients.add(input())

ans = []
M = int(input())
for _ in range(M):
    name = input()
    col = int(input())
    receipt = set()
    for _ in range(col):
        receipt.add(input())

    if receipt <= ingredients:
        ans.append(name)

if ans:
    ans.sort()
    print('\n'.join(ans))
else:
    print('Готовить нечего')
