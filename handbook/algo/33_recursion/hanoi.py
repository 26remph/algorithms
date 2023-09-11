def HanoiTowers(n, fromPeg, toPeg):
    if n == 1:
        print(f'Move disk from peg {fromPeg} to {toPeg}')
        return
    unusedPeg = 6 - fromPeg - toPeg
    HanoiTowers(n - 1, fromPeg, unusedPeg)
    print(f'{n}>Move disk from peg {fromPeg} to {toPeg}')
    HanoiTowers(n - 1, unusedPeg, toPeg)


HanoiTowers(4, 1, 3)
