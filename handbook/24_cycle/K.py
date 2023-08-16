def solution(num):

    if num == 1:
        return False

    if num == 2:
        return True

    i = num - 1
    while num % i != 0:
        i -= 1

    return True if i == 1 else False


if __name__ == '__main__':
    n = int(input())
    cnt = 0
    for _ in range(n):
        # print(solution(int(input())))
        cnt += 1 if solution(int(input())) else 0

    print(cnt)