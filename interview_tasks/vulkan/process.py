from multiprocessing.managers import BaseProxy


class TestPrintClass:
    def __init__(self):
        self.x = 100

    def __str__(self):
        return f'{type(self)}:{self.x}'


class MyAwesomeClassProxy(BaseProxy):

    _exposed_ = ('exposed_func', )

    def exposed_func(self):
        self._callmethod('exposed_func')



test = TestPrintClass()
print(test)