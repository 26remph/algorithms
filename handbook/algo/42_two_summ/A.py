def solution(a, b):
    return a + b


if __name__ == "__main__":
    a, b = map(int, input().split())
    print(solution(a, b))

    tests = (
        [0, 0, 0],
        [1, 2, 3],
        [9, 9, 18],
    )
    for a, b, ans in tests:
        assert a + b == solution(a, b), f"{a=}, {b=}, {ans=}"
