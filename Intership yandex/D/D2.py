
# from Levenshtein import distance
#
# n = 5
# words = ['rom', 'bom', 'dom', 'bot', 'rot']
# parent = 'rom'
#
# edits = [w for w in words if distance(parent, w) == 1]
# print(edits)

import itertools
import time

test_files = ['input4_D.txt']
for i in range(len(test_files)):
    name = test_files[i]
    words = []
    with open(name, 'r') as f:
        n = int(f.readline())
        for _, line in enumerate(f, 2):
            words.append(line.rstrip())

start_time = time.time()

result = itertools.combinations(words, 2)
cnt = 0
for item in result:
    cnt += 1

print("--- %s seconds ---" % (time.time() - start_time))
print(cnt)