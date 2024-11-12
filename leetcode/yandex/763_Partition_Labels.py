import collections

from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = {v: k for k, v in enumerate(s)}
        pointer = 0
        col = 0
        ans = []
        for i in range(len(s)):
            pointer = max(pointer, d[s[i]])
            col += 1
            if i == pointer:
                ans.append(col)
                col = 0
        print(ans)

    def my_partitionLabels(self, s: str) -> List[int]:
        total = set()
        part = 0
        d = collections.defaultdict(int)
        p = [0] * 26
        for i in range(len(s)):
            if s[i] not in total:
                part += 1
                p[ord(s[i]) - ord("a")] = part
                d[part] += 1
                # print(s[i], p)
                # print(f'{part=}, {p=}, {d=}, {total=}')
            else:
                d[part] += 1

                if p[ord(s[i]) - ord("a")] < part:
                    # print(s[i], part, p, d)
                    # print('p[si]=', p[ord(s[i]) - ord('a')])

                    part = p[ord(s[i]) - ord("a")]
                    # conc = []
                    col = 0
                    for key, val in d.items():
                        if key > part:
                            col += val
                            d[key] = 0

                    d[part] += col
                    # print(conc, d)

                    for k in range(len(p)):
                        if p[k] > part:
                            p[k] = part

            total.add(s[i])

        # print(p)
        # print(d)
        ans = []
        for key in sorted(d.keys()):
            if d[key]:
                ans.append(d[key])
        return ans


if __name__ == "__main__":
    # s = "ababcbacadefegdehijhklij"
    # s = "qvmwtmzzse"
    # s = "eccbbbbdec"
    sol = Solution()
    print(sol.partitionLabels(s))
