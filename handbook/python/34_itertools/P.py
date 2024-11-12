import itertools


names = {"пики": "пик", "трефы": "треф", "черви": "червей", "буби": "бубен"}

suits = ["буби", "пики", "трефы", "черви"]
cards = ["10", "2", "3", "4", "5", "6", "7", "8", "9", "валет", "дама", "король", "туз"]
need_suit = input()
cards.remove(input())

cnt = 0
for c in itertools.permutations(itertools.product(cards, suits), 3):
    if any([need_suit in c[0], need_suit in c[1], need_suit in c[2]]):
        print(", ".join([f"{x[0]} {names[x[1]]}" for x in c]))
        cnt += 1

    if cnt == 10:
        break
