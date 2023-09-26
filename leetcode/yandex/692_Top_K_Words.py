import collections
import heapq
from typing import List


class Solution:

    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        cnt = collections.Counter(words)
        heap = [(-f, w) for w, f in cnt.items()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]

    def low_topKFrequent(self, words: List[str], k: int) -> List[str]:
        cnt = collections.Counter(words)
        ans = cnt.most_common()
        ans.sort(key=lambda x: (-x[1], x[0]))
        return [x[0] for x in ans[:k]]


if __name__ == '__main__':
    # words = ["i","love","leetcode","i","love","coding"]
    words = ["i","love","leetcode","i","love","coding"]
    k = 3
    sol = Solution()
    print(sol.topKFrequent(words, k))

