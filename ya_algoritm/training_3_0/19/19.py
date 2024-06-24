

class Heap:
    _seq = []

    def push(self, *args):
        self._seq.append(int(args[0]))

        i = len(self._seq) - 1
        while i > 0:
            if self._seq[(i - 1) // 2] < self._seq[i]:
                self._seq[(i - 1) // 2], self._seq[i] = self._seq[i], self._seq[(i - 1) // 2]
            else:
                break
            i = (i - 1) // 2

        # print(self._seq)

    def pop(self):
        i = 0
        val = self._seq[i]

        last = self._seq.pop()
        if len(self._seq) == 0:
            return val

        self._seq[i] = last
        while True:
            lch = (self._seq[2 * i + 1], 2 * i + 1) if len(self._seq) > 2 * i + 1 else None
            rch = (self._seq[2 * i + 2], 2 * i + 2) if len(self._seq) > 2 * i + 2 else None

            if lch or rch:
                if lch and rch:
                    max_ch = max(lch, rch, key=lambda x: x[0])
                else:
                    max_ch = lch
                if max_ch[0] > self._seq[i]:
                    self._seq[i], self._seq[max_ch[1]] = self._seq[max_ch[1]], self._seq[i]
                else:
                    break
                i = max_ch[1]
            else:
                break

        # print('val:', val, self._seq)
        return val


n = int(input())
funcs = {0: 'push', 1: 'pop'}
h = Heap()
for _ in range(n):
    key, *param = input().strip().split(' ')
    func = getattr(h, funcs.get(int(key)))
    ans = func(*param)
    if ans is not None:
        print(ans)
