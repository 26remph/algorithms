# import time
from collections import Counter


word_one: str = input().strip()
word_two: str = input().strip()

# start_time = time.time()

f = [val for ind, val in enumerate(word_one) if val != word_two[ind]]
cnt = Counter(f)

for ind, ch in enumerate(word_two):
    if ch == word_one[ind]:
        print('correct')
        continue

    if cnt[ch] > 0:
        print('present')
        cnt.subtract(ch)
    else:
        print('absent')

# print("--- %s seconds ---" % (time.time() - start_time))
