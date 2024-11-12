receipt: dict[str, dict[str, int]] = {
    "эспрессо": {"coffee": 1},
    "капучино": {"coffee": 1, "milk": 3},
    "макиато": {"coffee": 2, "milk": 1},
    "кофе по-венски": {"coffee": 1, "cream": 2},
    "латте макиато": {"coffee": 1, "milk": 2, "cream": 1},
    "кон панна": {"coffee": 1, "cream": 1},
}


def order(*drinks: str) -> str:
    global in_stock
    ans = []
    for drink in drinks:
        ingredients = receipt.get(drink.lower().strip(), {})

        check = True
        for ing, need in ingredients.items():
            if not (in_stock.get(ing, 0) and in_stock[ing] >= need):
                check = False
                break

        if check:
            ans.append(drink.strip())
            for ing, need in ingredients.items():
                in_stock[ing] -= need

            return "\n".join(ans)

    ans = "К сожалению, не можем предложить Вам напиток"
    return ans


if __name__ == "__main__":
    # test 1
    # in_stock = {"coffee": 1, "milk": 2, "cream": 3}
    # print(order("Эспрессо", "Капучино", "Макиато", "Кофе по-венски", "Латте Макиато", "Кон Панна"))
    # print(order("Эспрессо", "Капучино", "Макиато", "Кофе по-венски", "Латте Макиато", "Кон Панна"))
    # test 2
    # in_stock = {"coffee": 4, "milk": 4, "cream": 0}
    # print(order("Капучино", "Макиато", "Эспрессо"))
    # print(order("Капучино", "Макиато", "Эспрессо"))
    # print(order("Капучино", "Макиато", "Эспрессо"))

    print("--check--")
    # in_stock = {"coffee": 100, "milk": 400, "cream": 100}
    # print(order('Эспрессо ', 'Капучино ', ' Макиато ', ' Кофе по-венски ', ' Латте Макиато ', ' Кон Панна '))
    # print(order('Капучино ', ' Макиато ', ' Кофе по-венски ', ' Латте Макиато ', ' Кон Панна '))
    # print(order(' Макиато ', ' Кофе по-венски ', ' Латте Макиато ', ' Кон Панна '))
    # print(order(' Кофе по-венски ', ' Латте Макиато ', ' Кон Панна '))
    # print(order(' Латте Макиато ', ' Кон Панна '))
    # print(order(' Кон Панна '))

    in_stock = {"coffee": 1, "milk": 0, "cream": 1}
    print(
        order(
            "Эспрессо ",
            "Капучино ",
            " Макиато ",
            " Кофе по-венски ",
            " Латте Макиато ",
            " Кон Панна ",
        )
    )
