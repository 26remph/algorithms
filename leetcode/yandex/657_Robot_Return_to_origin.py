class Solution:
    def judgeCircle(self, moves: str) -> bool:
        dot = [0, 0]  # (l, r) (u, d)

        for n in moves:
            if n == "U":
                dot[1] += 1
            if n == "D":
                dot[1] -= 1
            if n == "L":
                dot[0] += 1
            if n == "R":
                dot[0] -= 1

        # return True if not dot[0] and not dot[1] else False
        return bool(not dot[0] and not dot[1])


if __name__ == "__main__":
    # s = 'UD'
    # s = 'LL'
    s = "UDLLRR"
    sol = Solution()
    print(sol.judgeCircle(s))
