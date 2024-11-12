def is_poli(s):
    if len(s) == 1:
        return 1

    j = len(s) - 1
    for i in range(len(s) // 2):
        if s[i] != s[j]:
            return 0
        j -= 1
    return 1


if __name__ == "__main__":
    N = int(input())
    ans = 0
    for _ in range(N):
        num = input()
        ans += is_poli(num)

    print(ans)
