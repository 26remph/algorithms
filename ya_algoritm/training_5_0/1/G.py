

def check_defense(i, j):
    step = 1
    while i > 0 and j > 0:
        # print(f'{step},{(i, j)}')
        i, j = j - i, i
        step += 1

    return step - 1 if bool(step % 2) else -1


def solider_attack(x, x1, y):
    remind = x1 - x
    # solider attacks
    x1 -= x
    x1 = max(0, x1)
    # barracks attack
    if remind < 0:
        y -= abs(remind)
        y = max(0, y)

    # enemy attacks
    x -= x1
    x = max(0, x)

    # produce solider
    if y > 0:
        x1 += p

    # print(f'->{remind=}, {y=}, {x=}, {x1=}')
    return x, x1, y


def barracks_attack(x, x1, y, rnd):
    remind = y - x
    y -= x
    y = max(0, y)
    # solider attacks
    if remind < 0 and rnd != 1:
        x1 -= abs(remind)
        x1 = max(0, x1)

    # enemy attacks
    x -= x1
    x = max(0, x)

    # produce solider
    if y > 0:
        x1 += p

    # print(f'->{remind=}, {y=}, {x=}, {x1=}')
    return x, x1, y


def main():
    global x, y, p
    x1 = 0  # enemy solider
    rnd = 1  # game round
    flow_attacks = 2  # 1: solider -> barracks, 2: barracks -> solider
    gold_seq = 0.5 * (1 + pow(5, 0.5))  # win condition

    while True:

        # tactic
        if rnd != 1:
            if x1 == x:
                flow_attacks = 2
            elif y == 0:
                flow_attacks = 1
            elif x < y:
                flow_attacks = 1
                if x == x1:
                    flow_attacks = 2
            elif x1 - x + y <= 0:
                flow_attacks = 2
            elif x / (x1 - x + y) < gold_seq:
                flow_attacks = 1
                print(x / (x1 - x + y) < gold_seq, x / (x1 - x + y))
            else:
                print('---check variant')
                step_to_win_now = check_defense(x1 - x + y, x)
                next_x, next_x1, next_y = solider_attack(x, x1, y)
                print(f'{next_x=}, {next_x1=}, {next_y=}')
                step_to_win_next = check_defense(next_x1 - next_x + next_y, next_x)
                print(f'{step_to_win_next=}, {step_to_win_now=}')
                if step_to_win_now < step_to_win_next + 1 or step_to_win_next < 0:
                    flow_attacks = 2
                else:
                    flow_attacks = 1

        print(f'{rnd=}, {flow_attacks=}, {x=}, {x1=}, {p=}, {y=}')

        if flow_attacks == 1:
            x, x1, y = solider_attack(x, x1, y)
        else:
            x, x1, y = barracks_attack(x, x1, y, rnd)

        # total
        if not y and not x1:
            return rnd
        if not x:
            return -1

        #  next round
        rnd += 1


if __name__ == '__main__':
    # x, y, p = map(int, [input() for _ in range(0, 3)])
    x, y, p = 10, 11, 15
    assert main() == 4
    x, y, p = 1, 2, 1
    assert main() == -1
    x, y, p = 1, 1, 1
    assert main() == 1
    x, y, p = 25, 200, 10
    assert main() == 13
    x, y, p = 13, 81, 10
    assert main() == 23
    x, y, p = 1, 500, 1
    assert main() == -1
    x, y, p = 250, 500, 187
    assert main() == 4
    x, y, p = 250, 500, 208
    assert main() == 5
    x, y, p = 300, 301, 484
    assert main() == 6
    x, y, p = 250, 500, 249
    assert main() == 101, '39'
    x, y, p = 3000, 5000, 3000
    assert main() == -1, '148'

    print(main())
    # print(timeit('main()', number=1, globals=globals()))
    print('pass')
