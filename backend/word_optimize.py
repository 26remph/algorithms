import time
from collections import Counter

word_one: str = input().strip()
word_two: str = input().strip()

start_time = time.time()
# use_index: set = set()

# f = filter(
#     lambda x: True if word_one[x[0]] != word_two[x[0]] else False, word_one
# )

f = [val for ind, val in enumerate(word_one) if val != word_two[ind]]
cnt = Counter(f)
# print(list(f), type(f))
# print(cnt)

# cnt.subtract('B')
# print(cnt)
# print(cnt['B'])

for ind, ch in enumerate(word_two):
    if ch == word_one[ind]:
        print('correct')
        continue

    if cnt[ch] > 0:
        print('present')
        cnt.subtract(ch)
    else:
        print('absent')

print("--- %s seconds ---" % (time.time() - start_time))
