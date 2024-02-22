def can_eat(knight: tuple, piece: tuple) -> bool:
    bit = {
        (knight[0] + 2, knight[1] + 1),
        (knight[0] + 2, knight[1] - 1),
        (knight[0] - 2, knight[1] + 1),
        (knight[0] - 2, knight[1] - 1),
        (knight[0] + 1, knight[1] + 2),
        (knight[0] - 1, knight[1] + 2),
        (knight[0] + 1, knight[1] - 2),
        (knight[0] - 1, knight[1] - 2),
    }
    if piece in bit:
        return True

    return False


if __name__ == '__main__':
    print(can_eat((2, 1), (4, 2)))
    print(can_eat((5, 5), (6, 6)))
