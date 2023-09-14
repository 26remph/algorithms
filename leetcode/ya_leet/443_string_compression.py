from typing import List


class Solution:

    def compress(self, chars: List[str]) -> int:

        cnt = 0
        ch = chars[0]
        total = 0
        for i in range(len(chars)):

            if chars[i] == ch:
                cnt += 1
            else:
                if cnt > 1:
                    chars[total] = ch
                    total += 1
                    for x in str(cnt):
                        chars[total] = x
                        total += 1
                else:
                    chars[total] = ch
                    total += 1

                cnt = 1
                ch = chars[i]

        if cnt > 1:
            chars[total] = ch
            total += 1
            for x in str(cnt):
                chars[total] = x
                total += 1
        else:
            chars[total] = ch
            total += 1

        while len(chars) != total:
            chars.pop()

        # print(chars)
        return len(chars)

    def compress_low(self, chars: List[str]) -> int:

        cnt = 0
        ch = chars[0]
        ans = []

        for i in range(len(chars)):

            if chars[i] == ch:
                cnt += 1
            else:
                if cnt > 1:
                    ans.append(ch)
                    ans.extend([x for x in str(cnt)])
                    chars[0] = '1'
                else:
                    ans.append(ch)
                cnt = 1
                ch = chars[i]

        if cnt > 1:
            ans.append(ch)
            ans.extend([x for x in str(cnt)])
        else:
            ans.append(ch)

        chars.clear()
        chars.extend(ans)

        return len(''.join(ans))


if __name__ == '__main__':
    tests = (
        (["a","a","b","b","c","c","c"], 6),
        (["a"], 1),
        (["a","b","b","b","b","b","b","b","b","b","b","b","b"], 4),
        (["a"], 1),
    )
    sol = Solution()
    for s, res in tests:
        # print(sol.compress(s))
        assert sol.compress(s) == res, f'{s=}, {res}'

