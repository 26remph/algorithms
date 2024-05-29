def is_palindrome(s: int | str | tuple | list) -> bool:
    if isinstance(s, int):
        s = str(s)
    return s == s[::-1]


if __name__ == '__main__':
    print(is_palindrome(123))
    print(is_palindrome([1, 2, 1, 2, 1]))
