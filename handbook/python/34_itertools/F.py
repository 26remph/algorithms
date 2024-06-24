from itertools import product


suit = ['пик', 'треф', 'бубен', 'червей']
nominal = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз']

suit.remove(input())
for n, s in product(nominal, suit):
    print(n, s)
