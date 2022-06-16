import time

word_one: str = input().strip()
word_two: str = input().strip()

# start_time = time.time()
use_index: set = set()

for ind, ch in enumerate(word_two):
    if ch == word_one[ind]:
        use_index.add(ind)
        print('correct')
    else:
        ind_find: int = 0
        pos = 0
        while True:
            pos = word_one.find(ch, ind_find, len(word_one))

            if pos == - 1:
                break

            if pos in use_index:
                ind_find = pos + 1
                continue
            else:
                use_index.add(pos)
                break

        if pos == -1 or word_one[pos] == word_two[pos]:
            print('absent')
        else:
            print('present')

# print("--- %s seconds ---" % (time.time() - start_time))
