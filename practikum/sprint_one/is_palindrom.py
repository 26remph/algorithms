import string


def is_palindrome(line: str) -> bool:
    line = line.strip()
    for p in string.punctuation:
        line = line.replace(p, "")

    phrase = line.lower().replace(" ", "")
    rev_word = "".join(reversed(list(phrase)))
    return phrase == rev_word


print(is_palindrome(input().strip()))
