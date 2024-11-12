v1, v2, v3 = int(input()), int(input()), int(input())
PETJA, TOLJA, VASJA = "Петя", "Толя", "Вася"
PLACE_ONE, PLACE_TWO, PLACE_THREE = "I", "II", "III"
TAB = " "
n_one, n_two, n_three = PETJA, VASJA, TOLJA

if v1 > v3 > v2:
    n_one, n_two, n_three = PETJA, TOLJA, VASJA
elif v2 > v1 > v3:
    n_one, n_two, n_three = VASJA, PETJA, TOLJA
elif v2 > v3 > v1:
    n_one, n_two, n_three = VASJA, TOLJA, PETJA
elif v3 > v1 > v2:
    n_one, n_two, n_three = TOLJA, PETJA, VASJA
elif v3 > v2 > v1:
    n_one, n_two, n_three = TOLJA, VASJA, PETJA

print(f"{n_one:^24}")
print(f"{n_two:^8}")
print(f"{TAB:16}{n_three:^8}")
print(f"{PLACE_TWO:^8}{PLACE_ONE:^8}{PLACE_THREE:^8}")
