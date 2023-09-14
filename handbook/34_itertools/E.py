import itertools

lst1 = input().split(', ')
lst2 = input().split(', ')
lst3 = input().split(', ')


for n, name in enumerate(sorted(itertools.chain(lst1, lst2, lst3)), 1):
    print(f'{n}. {name}')
