'''A. Строительство лесенок'''
'''https://contest.yandex.ru/contest/39359/problems/A/'''

n = int(input())

sum = 0
i = 0

while sum <= n:
    i += 1
    sum += i

print(i - 1)
