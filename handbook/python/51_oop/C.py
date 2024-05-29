class RedButton:
    def __init__(self, counter: int = 0) -> None:
        self.counter = counter

    def click(self) -> None:
        self.counter += 1
        print('Тревога!')

    def count(self) -> int:
        return self.counter


if __name__ == '__main__':
    first_button = RedButton()
    second_button = RedButton()
    for time in range(5):
        if time % 2 == 0:
            second_button.click()
        else:
            first_button.click()
    print(first_button.count(), second_button.count())