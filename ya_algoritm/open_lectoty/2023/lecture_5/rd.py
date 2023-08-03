class Checker(list):

    _flags: int = 0

    def __setitem__(self, key, value):
        prev = self[key]
        super(Checker, self).__setitem__(key, value)
        now = self[key]

        if prev < 3 and now >= 3:
            self._flags += 1
        elif prev > 3 and now < 3:
            self._flags -= 1

        print('fl:', self._flags)

    def is_continuous(self):
        return True if self._flags >= 4 else False


ch = Checker([0] * 4)
ch[0] = 4
ch[1] = 4
ch[2] = 4
ch[3] = 3
print(ch)
print(ch.is_continuous())
ch[3] = 5
print(ch)
print(ch.is_continuous())
ch[3] = 1
ch[2] = 1
print(ch)
print(ch.is_continuous())
ch[3] = 5
print(ch)
print(ch.is_continuous())
ch[2] = 6
print(ch)
print(ch.is_continuous())
