n = int(input())
arr = list(map(int, input().strip().split(' ')))
arr.sort()

if len(arr) == 2:
    print(arr[1] - arr[0])
elif len(arr) == 3:
    print(arr[2] - arr[1] + arr[1] - arr[0])
elif len(arr) == 4:
    print(arr[3] - arr[2] + arr[1] - arr[0])
else:
    dp = [0, arr[1] - arr[0], arr[2] - arr[1] + arr[1] - arr[0], arr[3] - arr[2] + arr[1] - arr[0]]
    for i in range(4, len(arr)):
        sum1 = dp[i - 2] + arr[i] - arr[i - 1]
        sum2 = dp[i - 3] + (arr[i] - arr[i - 1]) + (arr[i - 1] - arr[i - 2])
        # print(sum1, sum2, arr[i])
        dp.append(min(sum1, sum2))

    print(dp[-1])
    # print('arr', arr)
