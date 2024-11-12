import collections


def main():
    T = int(input())

    V = set()
    W = collections.defaultdict(int)

    for _ in range(T):
        w = input()
        for ind in range(len(w) - 3):
            w1 = "".join([w[ind], w[ind + 1], w[ind + 2]])
            w2 = "".join([w[ind + 1], w[ind + 2], w[ind + 3]])
            V.add(w1)
            V.add(w2)
            W[(w1, w2)] += 1

    print(len(V))
    print(len(W))
    for key, val in W.items():
        print(key[0], key[1], val)


if __name__ == "__main__":
    main()
