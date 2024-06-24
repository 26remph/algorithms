def number_length(num: int) -> int:
    return len(str(num)) if num >= 0 else len(str(num)) - 1


if __name__ == '__main__':
    result = number_length(12345)
    print(result)
    result = number_length(-100500)
    print(result)
    result = number_length(-0)
    print(result)
