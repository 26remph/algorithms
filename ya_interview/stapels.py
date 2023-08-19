def solution(s):

    steak = []
    close = ')}]'
    pairs = {
        '(': ')',
        '[': ']',
        '{': '}',
    }

    for i in range(len(s)):

        if s[i] in close:
            if steak:
                val = steak.pop()
                if pairs[val] != s[i]:
                    return False
            else:
                return False
        else:
            steak.append(s[i])

    if steak:
        return False

    return True


if __name__ == '__main__':
    test = [
        ('[]{}()', True),
        ('[{()}]', True),
        ('[{()}]', True),
        ('[{]}]', False)
    ]

    for s, ans in test:
        print(solution(s))
        assert solution(s) == ans, f'{ans=}, {s=}'