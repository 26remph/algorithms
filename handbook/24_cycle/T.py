def solution(n):

    max_ = sum(map(int, list(str(n)))), 10
    print(max_)
    for base in range(2, 10):
        ans = []
        num = n
        while num:
            ans.append(num % base)
            num = num // base

        max_ = max(max_, (sum(ans), base), key=lambda x: (x[0], -x[1]))
        print('base:', base, 'sum:', sum(ans), ans)

    return max_[1]


if __name__ == '__main__':
    N = int(input())
    print(solution(N))