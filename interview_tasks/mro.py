# 4
class A:
    def say(self):
        return 'a'


class B:
    def say(self):
        return 'b'


class C(A, B):
    pass


c = C()
print(c.say())