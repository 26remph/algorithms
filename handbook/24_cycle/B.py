def solution(n):

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(f'{j} * {i} = {j * i}')


if __name__ == '__main__':
    n = int(input())
    solution(n)
