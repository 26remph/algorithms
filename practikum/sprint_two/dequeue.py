# ID 69340518


class Deque:
    def __init__(self, n):
        self.__max_n = n
        self.__queue = [None] * n
        self.__tail = 0
        self.__head = 0
        self.__len = 0

    def is_empty(self):
        return self.__len == 0

    def push_back(self, x):
        if self.__len != self.__max_n:
            self.__queue[self.__tail] = x
            self.__tail = (self.__tail + 1) % self.__max_n
            self.__len += 1
        else:
            raise ValueError("error")

    def push_front(self, x):
        if self.__len != self.__max_n:
            self.__queue[self.__head - 1] = x
            self.__head = (self.__head - 1) % self.__max_n
            self.__len += 1
        else:
            raise ValueError("error")

    def pop_front(self):
        if self.is_empty():
            raise ValueError("error")

        x = self.__queue[self.__head]
        self.__queue[self.__head] = None
        self.__head = (self.__head + 1) % self.__max_n
        self.__len -= 1

        return x

    def pop_back(self):
        if self.is_empty():
            raise ValueError("error")

        x = self.__queue[self.__tail - 1]
        self.__queue[self.__tail - 1] = None
        self.__tail = (self.__tail - 1) % self.__max_n
        self.__len -= 1

        return x


if __name__ == "__main__":
    n = int(input())
    capacity = int(input())
    queue = Deque(capacity)

    for _ in range(n):
        command, *params = input().split(" ")
        func = getattr(queue, command)
        try:
            rez = func(*params)
            if rez is not None:
                print(rez)
        except ValueError as e:
            print(e)
