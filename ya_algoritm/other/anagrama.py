def solution(a, b):
    if len(a) != len(b):
        return False

    b = set(b)
    return all(ch in b for ch in a)


if __name__ == "__main__":
    a, b = input(), input()
    print(solution(a, b))
