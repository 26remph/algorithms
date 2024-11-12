from collections import defaultdict


friends = defaultdict(set)
while s := input():
    fr1, fr2 = s.split()
    friends[fr1].add(fr2)
    friends[fr2].add(fr1)

# pprint(friends)

for my in sorted(friends.keys()):
    far_friends = set()
    for f in friends[my]:
        far_friends.update(friends[f] - {my} - friends[my])

    ans = list(far_friends)
    ans.sort()
    print(f"{my}:", ", ".join(ans))
