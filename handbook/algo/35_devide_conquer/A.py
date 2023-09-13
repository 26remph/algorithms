def solution(a):

    for i in range(len(a)):
        min_ind = i
        for j in range(i + 1, len(a)):
            if a[j] < a[min_ind]:
                min_ind = j

        a[i], a[min_ind] = a[min_ind], a[i]

    return a


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(' '.join(map(str, solution(arr))))
