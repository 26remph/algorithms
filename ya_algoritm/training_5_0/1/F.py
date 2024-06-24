

def main():

    amount = 0
    odd_pos = -1
    is_pos_init = False
    for i in range(len(arr)):
        amount += arr[i]
        if arr[i] % 2 and not is_pos_init:
            is_pos_init = True
            odd_pos = i

    if amount % 2:
        return ''.join(sign)

    if odd_pos == len(arr) - 1:
        sign[-1] = '*'
    else:
        sign[odd_pos] = 'x'

    return ''.join(sign)


if __name__ == '__main__':
    _ = input()
    arr = list(map(int, input().split()))
    sign = ['+' for _ in range(len(arr) - 1)]
    print(main())

    # while True:
    #     # check
    #     arr = random.sample(range(0, 100), k=20)
    #     sign = ['+' for _ in range(len(arr) - 1)]
    #     main()
    #     c_arr = arr[:]
    #     m_sum = 0
    #     for i, s in enumerate(sign):
    #         if s == 'x':
    #             m_sum = c_arr[i] * c_arr[i+1]
    #             c_arr[i], c_arr[i+1] = 0, 0
    #
    #     check_sum = sum(c_arr) + m_sum
    #     assert check_sum % 2, f'{c_arr=}, {check_sum=}, {m_sum=}, {sign}'
    #     print(f'{c_arr=}, {check_sum=}, {m_sum=}, {sign}')
    #     print(f'{arr=}')
