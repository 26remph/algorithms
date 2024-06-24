class Programmer:

    rate = {'Junior': 10, 'Middle': 15, 'Senior': 20}

    def __init__(self, name: str, position: str):
        self.name = name
        self.position = position
        self.current_rate = self.rate[self.position]
        self.salary = {'Junior': 0, 'Middle': 0, 'Senior': 0}
        self.worked_time = 0

    def rise(self) -> None:
        keys = list(self.rate)
        cur_ind = keys.index(self.position)
        if cur_ind + 1 < len(self.rate):
            self.position = keys[cur_ind + 1]
            self.current_rate = self.rate[self.position]
        else:
            self.current_rate += 1

    def work(self, time: int) -> None:
        self.salary[self.position] += time * self.current_rate
        self.worked_time += time

    def info(self) -> str:
        return f'{self.name} {self.worked_time}ч. {sum(self.salary.values())}тгр.'
        # return f'{self.name}, {self.position=}, {self.worked_time=}, {self.current_rate=}, {self.salary=}, {sum(self.salary.values())}'


if __name__ == '__main__':
    programmer = Programmer('Васильев Иван', 'Junior')
    programmer.work(750)
    print(programmer.info())
    programmer.rise()
    programmer.work(500)
    print(programmer.info())
    programmer.rise()
    programmer.work(250)
    print(programmer.info())
    programmer.rise()
    programmer.work(250)
    print(programmer.info())
