_ = int(input())
print("".join(ch1 + ch2 for ch1, ch2 in zip(input(), input(), strict=False)))
