import random
import string

N = 10
chars = []
S = 100_000

with open('input4_D.txt', 'w+') as f:
    f.write(f'{S}\n')
    for _ in range(S):
        chars = []
        for _ in range(N):
            chars.append(random.choice(string.ascii_lowercase + string.ascii_uppercase))

        word = ''.join(chars)
        f.write(f'{word}\n')



