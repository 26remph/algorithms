import collections


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cnt_mag = collections.Counter(magazine)
        cnt_note = collections.Counter(ransomNote)
        cnt_mag.subtract(cnt_note)

        return min(cnt_mag.values()) >= 0
