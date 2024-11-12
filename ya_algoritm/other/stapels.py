def solution(seq):
    stack = []
    for ch in seq:
        if ch == "(":
            stack.append(ch)
        else:
            if stack:
                stack.pop()
            else:
                return False

    return not stack


if __name__ == "__main__":
    tests = [
        ("()", True),
        ("(", False),
        (")", False),
        ("", True),
        ("())(", False),
        ("(())", True),
        (")()", False),
        ("()()", True),
        ("(())", True),
        ("()()()", True),
        ("()(())", True),
        ("(())()", True),
        ("(()())", True),
        ("((()))", True),
    ]
    for s, ans in tests:
        assert solution(s) == ans, f"s: {s}, sol: {solution(s)}, ans: {ans}"

    print("pass")
