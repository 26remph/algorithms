numbers = [1, 2, 3, 4, 5]
# numbers = [number for number in range(16, 100, 4)]
# print(numbers)
print({x for x in numbers if str(pow(x, 0.5)).split(".")[1] == "0"})
