class Fraction:
    def __init__(self, *args) -> None:
        if isinstance(args[0], str):
            self.__num, self.__den = [int(c) for c in args[0].split('/')]
        else:
            self.__num = args[0]
            self.__den = args[1]
        self.__reduction()

    def __sign(self):
        return -1 if self.__num < 0 else 1

    def __neg__(self) -> 'Fraction':
        return Fraction(-self.__num, self.__den)

    def __add__(self, other) -> 'Fraction':
        common_denominator = self.__den * other.__den
        new = Fraction(1, 1)
        new.__num = self.__num * other.__den + other.__num * self.__den
        new.__den = common_denominator
        new.__reduction()
        return new

    def __sub__(self, other) -> 'Fraction':
        common_denominator = self.__den * other.__den
        new = Fraction(1, 1)
        new.__num = self.__num * other.__den - other.__num * self.__den
        new.__den = common_denominator
        new.__reduction()
        return new

    def __iadd__(self, other) -> 'Fraction':
        common_denominator = self.__den * other.__den
        self.__num = self.__num * other.__den + other.__num * self.__den
        self.__den = common_denominator
        self.__reduction()
        return self

    def __isub__(self, other) -> 'Fraction':
        common_denominator = self.__den * other.__den
        self.__num = self.__num * other.__den - other.__num * self.__den
        self.__den = common_denominator
        self.__reduction()
        return self

    def __mul__(self, other) -> 'Fraction':
        common_denominator = self.__den * other.__den
        new = Fraction(1, 1)
        new.__num = self.__num * other.__num
        new.__den = common_denominator
        new.__reduction()
        return new

    def __truediv__(self, other) -> 'Fraction':
        new = Fraction(self.__num, self.__den)
        new.__reduction()
        return new.__mul__(other.reverse())

    def __imul__(self, other) -> 'Fraction':
        common_denominator = self.__den * other.__den
        self.__num = self.__num * other.__num
        self.__den = common_denominator
        self.__reduction()
        return self

    def __itruediv__(self, other) -> 'Fraction':
        return self.__imul__(other.reverse())

    def _gcd(self, a, b) -> int:
        while b:
            a, b = b, a % b
        return abs(a)

    def __reduction(self) -> tuple:
        __gcd = self._gcd(self.__num, self.__den)
        self.__num //= __gcd
        self.__den //= __gcd

        if self.__den < 0:
            self.__num = -self.__num
            self.__den = abs(self.__den)
        return self.__num, self.__den

    def __str__(self) -> str:
        return f'{self.__num}/{self.__den}'

    def __repr__(self) -> str:
        return f"Fraction('{self.__num}/{self.__den}')"

    def numerator(self, *args) -> int:
        if len(args):
            self.__num = args[0] * self.__sign()
            self.__reduction()
        return abs(self.__num)

    def denominator(self, *args) -> int:
        if len(args):
            self.__den = args[0]
        self.__reduction()
        return abs(self.__den)

    def reverse(self) -> 'Fraction':
        return Fraction(self.__den, self.__num)