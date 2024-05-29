import itertools

names = {'пики': 'пик', 'трефы': 'треф', 'черви': 'червей', 'буби': 'бубен'}

suits = ['буби', 'пики', 'трефы', 'черви']
cards = ['10', '2', '3', '4', '5', '6', '7', '8', '9', 'валет', 'дама', 'король', 'туз']
need_suit = input()
cards.remove(input())
last_lyout = input()

# cnt = 0
is_print = False
for c in itertools.combinations(itertools.product(cards, suits), 3):
    if any([need_suit in c[0], need_suit in c[1], need_suit in c[2]]):
        cur = ', '.join([f'{x[0]} {names[x[1]]}' for x in c])
        # print(', '.join([f'{x[0]} {names[x[1]]}' for x in c]))
        # cnt += 1
        if is_print:
            print(cur)
            break

        if cur == last_lyout:
            is_print = True

