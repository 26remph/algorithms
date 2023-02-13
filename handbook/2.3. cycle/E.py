discount = 0.1
amount = 0.0

while (price := float(input())) != 0:
    amount += float(price) if float(price) < 500 else price * (1 - discount)

print(amount)

