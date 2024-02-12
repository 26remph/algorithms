"""Example: Iteretate for odd item in collection."""


class OddIterator:
    def __init__(self, container):
        self.container = container
        self.ind = -1

    def __next__(self):
        if self.ind < len(self.container.collection):
            while self.ind + 1 < len(self.container.collection):
                self.ind += 1
                if self.container.collection[self.ind] % 2:
                    return self.container.collection[self.ind]

        raise StopIteration


class OddIter:
    def __init__(self, collection):
        self.collection = collection

    def __iter__(self):
        return OddIterator(self)


def test_gen(coll):
    for v in coll:
        yield v


if __name__ == '__main__':
    arr = [1, 2, 4, 1, 7, 4, 6, 8, 1]

    for v in OddIter(arr):
        print('odd val:', v)