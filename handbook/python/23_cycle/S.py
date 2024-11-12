def solution(left, right):
    while left < right:
        mid = (left + right) // 2
        print(mid)
        ans = input()
        if ans == "Угадал!":
            break

        if ans == "Меньше":
            right = mid
        else:
            left = mid + 1

    print(left)


if __name__ == "__main__":
    left, right = 1, 1_000
    solution(left, right)
