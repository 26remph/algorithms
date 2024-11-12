def selection(a):
    for i in range(len(a)):
        min_ind = i
        for j in range(i + 1, len(a)):
            if a[j] < a[min_ind]:
                min_ind = j

        a[i], a[min_ind] = a[min_ind], a[i]

    return a


if __name__ == "__main__":
    arr = [7, 92, 87, 1, 4, 3, 2, 6]
    print(selection(arr))
