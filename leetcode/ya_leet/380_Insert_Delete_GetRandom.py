import random


class RandomizedSet:

    def __init__(self):
        self.last = 0
        self.store = {}
        self.ind = [0] * 1_000

    def insert(self, val: int) -> bool:
        if val in self.store:
            return False

        if self.last >= 1_000:
            self.ind += [0] * 1_000

        self.store[val] = self.last
        self.ind[self.last] = val
        self.last += 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.store:
            return False

        print(f'{self.store=}, {self.ind=}, {val=}, {self.last=}')

        ind = self.store[val]

        last_val = self.ind[self.last - 1]
        self.ind[ind] = last_val
        self.store[last_val] = ind
        del self.store[val]
        self.last -= 1

        print(f'{self.store=}, {self.ind=}, {val=}, {ind=}, {self.last=}')
        return True

    def getRandom(self) -> int:
        return self.ind[random.randint(0, self.last - 1)]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()


if __name__ == '__main__':
    rnd = RandomizedSet()
    print(rnd.remove(0))
    print(rnd.remove(0))
    print(rnd.insert(0))
    print(rnd.getRandom())
    print(rnd.remove(0))
    print(rnd.insert(0))
