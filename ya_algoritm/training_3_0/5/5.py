n = int(input())

word = [0] * 26

for i in range(n):
    word[i] = int(input())

# print('w:', word)

cnt = 0
inf = float("inf")
l_min = inf
ans = 0
isContinue = True

while isContinue:
    isContinue = False

    for i in range(26):
        if word[i]:
            cnt += 1
            l_min = min(l_min, word[i])
        else:
            if cnt > 1:
                ans += l_min * (cnt - 1)
                # print('cnt', cnt, 'l_min', l_min, 'i', i)
                for j in range(i - cnt, i):
                    word[j] -= l_min
                # print('word:', word)
                l_min = inf
                cnt = 0
                isContinue = True

            cnt = 0

    if cnt > 1:
        ans += l_min * (cnt - 1)
        # print('cnt:', cnt, 'l_min:', l_min, 'i:', i, 'ans:', ans)
        for j in range(i - cnt + 1, 26):
            word[j] -= l_min
        # print('w:', word)
        l_min = inf
        cnt = 0
        isContinue = True

print(ans)
