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
            else:
                step_to_win_now = check_defense(x1 - x + y, x)
                next_x, next_x1, next_y = solider_attack(x, x1, y)
                step_to_win_next = check_defense(next_x1 - next_x + next_y, next_x)
                if step_to_win_now < step_to_win_next + 1 or step_to_win_next < 0:
                    flow_attacks = 2
                else:
                    flow_attacks = 1

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


if __name__ == "__main__":
    x, y, p = map(int, [input() for _ in range(0, 3)])
    print(main())
