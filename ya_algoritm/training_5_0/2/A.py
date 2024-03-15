if __name__ == '__main__':
    k = int(input())
    x_min, x_max, y_min, y_max = float('inf'), float('-inf'), float('inf'), float('-inf')
    for _ in range(k):
        x, y = map(int, input().split())
        x_min = min(x_min, x)
        x_max = max(x_max, x)
        y_min = min(y_min, y)
        y_max = max(y_max, y)

    print(x_min, y_min, x_max, y_max)

