from collections import Counter


# words = {}
cnt = Counter()
with open("input.txt", encoding="utf8") as f:
    while line := f.readline().rstrip():
        cnt.update(line.split())
        # for word in line.split():
        #     if words.get(word):
        #         words[word] += 1
        #     else:
        #         words[word] = 1
# ans = []
# for key, value in words.items():
#     ans.append((value, key))

# print('cnt', cnt)
# ans.sort(key=lambda x: (-x[0], x[1]))
# print(ans)
# for word in ans:
#     print(word[1])
for rez in sorted(cnt.most_common(), key=lambda x: (-x[1], x[0])):
    print(rez[0])
