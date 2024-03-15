import itertools
import random
import time
import timeit
from collections import deque
from functools import lru_cache


def merge(lst1: deque, lst2: deque):

    # deque test
    result = deque()
    while lst1 or lst2:
        if not lst1:
            return result + lst2
        elif not lst2:
            return result + lst1

        # el1, el2 = lst1[0], lst2[0]
        # expr1 = el1[3] + el2[0]
        # expr2 = el2[3] + el1[0]
        expr1 = lst1[0][3] + lst2[0][0]
        expr2 = lst2[0][3] + lst1[0][0]

        if expr1 >= expr2:
            result.append(lst1.popleft())
        else:
            result.append(lst2.popleft())
    return result


def merge_sort(lst: deque):
    if len(lst) <= 1:
        return lst
    else:
        left = deque(itertools.islice(lst, 0, len(lst)//2))
        right = deque(itertools.islice(lst, len(lst)//2, len(lst)))
        return merge(merge_sort(left), merge_sort(right))


def main(good: deque, acid: deque):
    if len(good) == 1 and not acid or len(acid) == 1 and not good:
        if good:
            return good[0][0], [1]
        return acid[0][0], [1]

    h = 0
    max_h = float('-inf')
    order = []
    for b in merge_sort(good):
        h += b[0]
        max_h = max(h, max_h)
        h -= b[1]
        order.append(b[2])

    # print(f'good: {max_h=}, {good=}, {h=}')
    if acid:
        for i in range(len(acid)):
            order.append(acid[i][2])

    if good and acid:
        max_h = max(max_h, h + acid[0][0])
    elif not good:
        max_h = acid[0][0]

    # print(f'acid: {max_h=}, {acid=}')

    return max_h, order


if __name__ == '__main__':

    with open('input.txt', encoding='UTF-8') as f:
        n = int(f.readline().rstrip())
        good_b = deque()
        acid_b = deque()
        max_acid = float('-inf')
        cnt = 1
        for row in f:
            ai, bi = map(int, row.rstrip().split())
            if ai < bi:
                if ai > max_acid:
                    max_acid = ai
                    acid_b.appendleft((ai, bi, cnt, ai - bi))
                else:
                    acid_b.append((ai, bi, cnt, ai - bi))
            else:
                good_b.append((ai, bi, cnt, ai - bi))
            cnt += 1
        ans = main(good_b, acid_b)
        print(f'{ans[0]}\n{" ".join(map(str, ans[1]))}')
        # print(f'{main(good_b, acid_b)=}')

    # speed test
    # start = time.time()
    # with open('30.file', encoding='UTF-8') as f:
    #     n = int(f.readline().strip())
    #     good_b = deque()
    #     acid_b = deque()
    #     cnt = 1
    #     max_acid = float('-inf')
    #     for row in f:
    #         ai, bi = map(int, row.strip().split())
    #         if ai < bi:
    #             if ai > max_acid:
    #                 max_acid = ai
    #                 acid_b.appendleft((ai, bi, cnt, ai - bi))
    #             else:
    #                 acid_b.append((ai, bi, cnt, ai - bi))
    #         else:
    #             good_b.append((ai, bi, cnt, ai - bi))
    #         cnt += 1
    # print(time.time() - start)
    # print(timeit.timeit('main(good_b, acid_b)', number=1, globals=globals()))
    # print(f'{len(acid_b)=}, {len(good_b)=}')

    # test algo
    # for _ in range(10000):
    #     n = random.randint(1, 5)
    #     good_b = deque()
    #     acid_b = deque()
    #     max_acid = float('-inf')
    #     for i in range(1, n+1):
    #         x1, x2 = random.randint(0, 10), random.randint(0, 10)
    #         if x1 < x2:
    #             if x1 > max_acid:
    #                 max_acid = x1
    #                 acid_b.appendleft((x1, x2, i, x1 - x2))
    #             else:
    #                 acid_b.append((x1, x2, i, x1 - x2))
    #         else:
    #             good_b.append((x1, x2, i, x1 - x2))
    #
    #     arr = list(good_b) + list(acid_b)
    #     ans_lst = list(itertools.permutations(arr, len(arr)))
    #     ans = []
    #     for ind, prem in enumerate(itertools.permutations(arr, len(arr))):
    #         high = 0
    #         max_high = [float('-inf'), 0]
    #         for el in prem:
    #             high += el[0]
    #             if max_high[0] < high:
    #                 max_high[0] = max(high, max_high[0])
    #                 max_high[1] = ind
    #             high -= el[1]
    #         ans.append(max_high)
    #         print(f'{max_high=}, {ans_lst[max_high[1]]=}{list(prem)=}')
    #
    #     max_ans = max(ans, key=lambda x: x[0])
    #     print('-' * 50)
    #     print(f'{arr=}')
    #     print(f'{ans_lst=}')
    #     print(f'{ans=}, \n{max_ans=}, {ans_lst[max_ans[1]]=}')
    #     print(f'{main(good_b, acid_b)=}')
    #     assert main(good_b, acid_b)[0] == max_ans[0]



