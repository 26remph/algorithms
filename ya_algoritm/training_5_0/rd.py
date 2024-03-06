import statistics


def check_win(i, j):
    # i, j = 16, 26
    # i, j = 37, 60
    # i, j = 61, 99
    # i, j = 80, 99
    # i, j = 82, 133
    step = 1
    while i > 0 and j > 0:
        # print(f'{step},{(i, j)}')
        i, j = j - i, i
        step += 1

    # print(bool(step % 2))
    return bool(step % 2)


ans = []
for i in range(1, 5000):
    for j in range(i, 5000):
        # if 1.62 < j / i <= 1.625:
        #     ans.append((i, j, j - i, j / i))
        # if 1.61 < j / i <= 1.625:
        #     ans.append((i, j, j - i, j / i))
        if j / i < 0.5 * (1 + pow(5, 0.5)):
            ans.append((i, j, j - i, j / i))

# arr_diff = [el[2] for el in ans]
# avg = [el[3] for el in ans]
# print(f'{statistics.mean(avg)}')
# print('statistic:', f'{statistics.mean(arr_diff)=}, {statistics.harmonic_mean(arr_diff)=}')

nums = set([(el[0], el[1]) for el in ans])
# print(ans)
# print('ans:', f'{len(ans)=}')
# print(nums)

print('---')
cnt = 0
for n1, n2 in nums:
    res = check_win(n1, n2)
    if res:
        cnt += 1
        print(f'{(n1, n2, n2 / n1)}')

print('pass')
print('win in:', cnt)
print((2584, 4181) in nums)
# print(check_win(2548, 4181))
# print(check_win(3, 2), 3 / 2)
print(0.5 * (1 + pow(5, 0.5)))
print(0.5 * (1 + pow(5, 0.5)) == 0.5 * (1 + pow(5, 0.5)))
