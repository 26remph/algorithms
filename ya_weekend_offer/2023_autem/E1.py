def solution():
    lst.sort(key=lambda x: x[1])
    ans = []
    for i, _ in lst:
        enrolled = False
        for p in student[i]:
            if program[p] > 0:
                program[p] -= 1
                ans.append((i, p))
                enrolled = True
                break

        if not enrolled:
            ans.append((i, -1))

    ans.sort(key=lambda x: x[0])
    return " ".join(map(str, [progr for _, progr in ans]))


if __name__ == "__main__":
    n, k = map(int, input().split())
    program = [0] + list(map(int, input().split()))
    lst = []
    student = {}
    for i in range(n):
        r, _, *desire = list(map(int, input().split()))
        student[i] = desire
        lst.append((i, r))

    print(solution())
