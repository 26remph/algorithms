from collections import deque


k1 = deque(map(int, input().strip().split(" ")))
k2 = deque(map(int, input().strip().split(" ")))

cnt = 0
while k1 and k2:
    card1 = k1.popleft()
    card2 = k2.popleft()

    pair = (card1, card2)

    match pair:
        case (9, 0):
            k2.extend(pair)
        case (0, 9):
            k1.extend(pair)
        case (card1, card2) if pair[0] > pair[1]:
            k1.extend(pair)
        case (card1, card2) if pair[0] < pair[1]:
            k2.extend(pair)

    cnt += 1
    if cnt >= 1_000_000:
        print("botva")
        break

if k1 and cnt < 1_000_000:
    print("first", cnt)

if k2 and cnt < 1_000_000:
    print("second", cnt)
