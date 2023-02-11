def transform(s: str):
    if not s:
        return ''
    result = [s[0], 0]
    for i in s[1:]:
        if i != result[-2]:
            result.extend([i, 0])
        else:
            result[-1] += 1

    print(result)
    return ''.join(result)


print(transform('AAAAAAAABBBBBCCCCCCC'))

# row = 'AZZZZZ'
# assert transform(row) == 'AZ5'
