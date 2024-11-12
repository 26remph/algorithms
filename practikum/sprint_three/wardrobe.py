n = int(input())
if n > 0:
    wardrobe = list(map(int, input().split(" ")))

    NUM_COLOR = 3
    colors = [0] * NUM_COLOR
    for color in wardrobe:
        colors[color] += 1

    for color, num in enumerate(colors):
        print((str(color) + " ") * num, end="")
