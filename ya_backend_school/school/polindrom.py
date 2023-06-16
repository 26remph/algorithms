def main():
    ans = ''
    s = input()

    if len(s) == 1:
        return ans

    for i in range(len(s) // 2):
        if s[i] != 'a':
            return s[:i] + 'a' + s[i+1:]

    return s[:-1] + 'b'


if __name__ == '__main__':
    print(main())
