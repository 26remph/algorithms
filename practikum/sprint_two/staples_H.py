from typing import List

pair_staples = {
    '{': '}',
    '[': ']',
    '(': ')',
}

stack: List[int] = []

def is_corect_backet_seq(seq):
    if not seq:
        return True

    for elem in seq:

        closed_staples = pair_staples.get(elem)

        if closed_staples is None:

            if not stack:
                return False

            last = stack.pop()
            last_closed = pair_staples.get(last)

            if not(last_closed and last_closed == elem):
                return False
        else:
            stack.append(elem)

    return stack == []


seq = input().strip()
print(is_corect_backet_seq(seq))
