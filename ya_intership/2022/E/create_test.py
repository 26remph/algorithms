import random
import sys


N = 200_000
SUM_N_LIMIT = 1_000_000


def gen_string(n):
    return (
        # ''.join(random.choice(string.ascii_lowercase) for _ in range(n)))
        ''.join(str(random.randint(1, n)) for _ in range(n)))


K = 10

arr = []

_sum = SUM_N_LIMIT + 1
cnt = 0
while _sum > SUM_N_LIMIT:
    arr = []
    for _ in range(K):
        x = random.randint(1, N)
        arr.append(x)
    _sum = sum(arr)
    cnt += 1
    print('x', end='')

print(f'\n{sum(arr)}')
print(arr)

syze_of_x = 0
full_data = []
for i in arr:
    vector = []
    for _ in range(i):
        x = random.randint(1, 20)
        syze_of_x += sys.getsizeof(x)
        vector.append(x)
    full_data.append(vector)


with open('data.txt', 'w') as f:
    f.write(str(K) + '\n')
    for row in full_data:
        f.write(str(len(row)) + ' ')
        f.write(' '.join(list(map(str, row))))
        f.write('\n')


with open('query.txt', 'w') as f:
    f.write(f'{N}\n')
    for _ in range(N):
        ing_A = random.randint(1, 100_000)
        ing_B = random.randint(1, 100_000)
        key = random.randint(1, 20)
        query = f'{ing_A} {ing_B} {key}\n'
        f.write(query)

# print(full_data)
print(f'size_of_arr: {sys.getsizeof(full_data):,} bytes')
print(f'size_of_x: {syze_of_x // 1000:,} kbytes')

# int_ch = '1000000100000010000001000000'
# int_int = 1_000_000

# print(sys.getsizeof(int_ch))
# print(sys.getsizeof(int_int) * 4)


# start_time = time.time()
# arr = []
# for _ in range(N):
#     arr.append(gen_string())
#
# print(f'size_of_arr: {sys.getsizeof(arr) // 1000:,} kbytes')
# print(f'read time: {time.time() - start_time} seconds')