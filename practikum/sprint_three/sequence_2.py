def merge_sort(seq, s):

    result = []
    s_ind = 0
    for ch in seq:
        if ch != s[s_ind]:
            continue

        result.append(ch)
        if s_ind < len(s) - 1:
            s_ind += 1
        else:
            break

    return result

s = input()
t = input()
rez = ''.join(merge_sort(t, s))
print(s in rez)
