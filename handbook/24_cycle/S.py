def solution(n):

    width = len(str(n // 2 + 1))

    left = []
    for i in range(1, n + 1):

        row = []
        if i < n // 2 + 1:
            row += left
            for _ in range(len(left), n - i + 1):
                row.append(str(i))

            row += left[::-1]

            left.append(str(i))
        else:

            row += left

            delta = 0 if n % 2 != 0 else -1
            for j in range(len(left), i + delta):
                row.append(str(n - i + 1))

            row += left[::-1]

            if left:
                left.pop()

        for ind in range(len(row)):
            print(f'{row[ind]:^{width + 1}}', end='')
        print('')


if __name__ == '__main__':
    N = int(input())
    solution(N)