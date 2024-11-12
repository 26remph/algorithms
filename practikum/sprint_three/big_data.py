def is_first_num(num_1, num_2):
    checksum_1 = int(str(num_1) + str(num_2))
    checksum_2 = int(str(num_2) + str(num_1))

    return checksum_1 > checksum_2


def get_bigdata(array, less):
    for i in range(1, len(array)):
        item_to_insert = array[i]
        j = i
        while j > 0 and less(item_to_insert, array[j - 1]):
            array[j] = array[j - 1]
            j -= 1
        array[j] = item_to_insert
    return array


n = int(input())
arr = list(map(int, input().split(" ")))

rez = get_bigdata(arr, is_first_num)
print("".join(map(str, rez)))
