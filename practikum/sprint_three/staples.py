
def is_correct(prefix):
    stack = []
    for ch in prefix:
        if ch == '(':
            stack.append(ch)
        else:
            if stack:
                stack.pop()
            else:
                return False

    return True if not stack else False


def get_binary(n, prefix=''):

    if n == 0:
        return print(prefix) if is_correct(prefix) else None
    else:
        get_binary(n - 1, prefix + '(')
        get_binary(n - 1, prefix + ')')


n = int(input())
get_binary(n * 2)
