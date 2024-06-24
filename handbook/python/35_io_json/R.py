# import os
import math


d = {
    0: 'Б',
    1: 'КБ',
    2: 'МБ',
    3: 'ГБ',
    4: 'ТБ'
}

fn = input()
with open(fn, 'rb') as f:
    size_b = 0
    while s := f.read(1024):
        size_b += len(s)

# size_b = 9_751_756
suffix = 0
while size_b >= 1024:
    size_b /= 1024
    suffix += 1

if math.ceil(size_b) >= 1024:
    size_b = size_b / 1024
    suffix += 1

print(f'{math.ceil(size_b)}{d[suffix]}')
