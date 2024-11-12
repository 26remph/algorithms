# n = int(input())
import time


test_files = ["input1_D.txt", "input2_D.txt", "input3_D.txt"]
# test_files = ['input5_D.txt']
for i in range(len(test_files)):
    name = test_files[i]
    words = []
    start_time = time.time()
    with open(name, "r") as f:
        n = int(f.readline())
        for _, line in enumerate(f, 2):
            words.append(line.rstrip())
    print("--- %s seconds ---" % (time.time() - start_time))

    # words = []
    # for i in range(n):
    #     w1 = input()
    #     words.append(w1)
    print(words)
    words.sort()
    print("--- %s seconds ---" % (time.time() - start_time))

    # print(words, 'len=', n)

    i, j = 0, 0
    cnt = 0

    while i < n:
        j = i + 1
        while j < n:
            mis = 0
            w1 = words[i]
            w2 = words[j]
            # print(w1, w2)
            for k in range(len(w1)):
                if w1[k] != w2[k]:
                    mis += 1

            if 0 < mis < 2:
                cnt += 1

            j += 1
        i += 1
        print("--- %s seconds ---" % (time.time() - start_time))

    print(cnt)
    print("--- %s seconds ---" % (time.time() - start_time))
