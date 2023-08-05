def solution(a, b):

    if len(a) != len(b):
        return False

    b = set(b)
    for ch in a:
        if ch not in b:
            return False

    return True


if __name__ == '__main__':
    a, b = input(), input()
    print(solution(a, b))