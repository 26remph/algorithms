
def solution(arr):
    val = max(arr, key=lambda x: (x[2], x[0]))
    return val[1]


if __name__ == '__main__':
    N = int(input())
    arr = []
    for i in range(N):
        name, ch = input(), input()
        arr.append((i, name, sum(int(w) for w in ch)))
    print(solution(arr))