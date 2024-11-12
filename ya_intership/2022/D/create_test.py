import random


MODE = {False: "data_create", True: "query"}

mode = bool(int(input("Mode data create (0) - data, (1) - query\n")))
n = int(input("How interval create?\n"))

RIGHT_EDGE = 1_000_000_000

with open(f"{MODE.get(mode)}.txt", "w") as f:
    f.write(str(n))

    for _ in range(n):
        start = random.randint(1, RIGHT_EDGE)
        end = random.randint(start, RIGHT_EDGE)

        param = random.randint(1, 2) if mode else random.randint(1, RIGHT_EDGE)

        f.write(f"\n{start} {end} {param}")
