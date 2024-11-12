input_set = set()


def modern_print(s: str) -> None:
    if s not in input_set:
        input_set.add(s)
        print(s)


if __name__ == "__main__":
    modern_print("Hello!")
    modern_print("Hello!")
    modern_print("How do you do?")
    modern_print("Hello!")  # print(hash("c") > hash("b"), "c" < "b")
