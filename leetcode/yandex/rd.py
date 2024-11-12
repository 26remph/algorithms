import collections
import itertools


seq = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for c in itertools.combinations(seq, 1):
    print(c)

# seq = '((a(a)(((b(b)(((c(c)((('
# seq = 'AAAABBBCCD'
# for k, g in itertools.groupby(list(seq)):
#     print(k, list(g))


def sliding_window(iterable, n):
    # sliding_window('ABCDEFG', 4) --> ABCD BCDE CDEF DEFG
    it = iter(iterable)
    window = collections.deque(itertools.islice(it, n), maxlen=n)
    if len(window) == n:
        yield tuple(window)
    for x in it:
        window.append(x)
        yield tuple(window)


for w in sliding_window("abcdefg", 4):
    print(w)
