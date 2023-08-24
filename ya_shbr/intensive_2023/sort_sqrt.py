# task insertion
def solution(arr):

    res = [arr[0]]
    for i in range(1, len(arr)):

        flag = False
        res.append(arr[i])
        for j in range(len(res) - 1, 0, -1):
            if res[j-1] < res[j]:
                res[j-1], res[j] = res[j], res[j-1]
                flag = True
            if not flag:
                break

    print(res)


if __name__ == '__main__':
    arr = [1, 4, 3, 4, 2]
    solution(arr)