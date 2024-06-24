street = list(map(int, input().split()))

left_coast = 1_000
right_cost = 1_000
indS = -1
route_cost = []

for i in range(len(street)):

    if street[i] == 2:
        indS = i

    if street[i] == 1:

        if indS >= 0:
            left_coast = i - indS

        for j in range(i, len(street)):
            if street[j] == 2:
                right_cost = j - i
                break

        route_cost.append(min(left_coast, right_cost))
        right_cost = 1_000

# print(route_cost)
print(max(route_cost))
