class OddIter:
    def __init__(self, collection):
        self.c = collection

    def __iter__(self):
        for val in self.c:
            if val % 2:
                yield val


if __name__ == "__main__":
    arr = [2, 4, 5, 6, 7, 11, 13]
    odd_iter = OddIter(arr)
    for odd_val in odd_iter:
        print("odd", odd_val)
