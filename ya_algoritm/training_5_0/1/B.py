def justify(g1, g2, g3, g4, fp):

    if g1 + g3 == g2 + g4:
        if first_play == 1:
            if g3 > g2:
                return 0
            else:
                return 1
        else:
            if g1 > g4:
                return 0
            else:
                return 1


def main():

    if g1 + g3 > g2 + g4:
        return 0
    elif g1 + g3 == g2 + g4:
        return justify(g1, g2, g3, g4, first_play)
    else:
        diff = g2 + g4 - g1 - g3
        goal = justify(g1, g2, g3 + diff, g4, first_play)
        return diff + goal


g1, g2 = map(int, input().split(":"))
g3, g4 = map(int, input().split(":"))
first_play = int(input())
print(main())


# if __name__ == '__main__':
#     g1, g2 = map(int, input().split(":"))
#     g3, g4 = map(int, input().split(":"))
#     first_play = int(input())
#     print(main())
