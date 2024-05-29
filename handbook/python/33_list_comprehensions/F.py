text = input()
d = {ch.lower(): sum([1 for x in text if x.lower() == ch.lower()]) for ch in text if ch.isalpha()}
print(d)