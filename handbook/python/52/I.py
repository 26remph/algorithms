import operator


class Fraction:
    def __init__(self, numer: str | int, denom: int | None = None):
        self.sign = 1
        if isinstance(numer, str):
            numer, denom = map(int, numer.split('/'))

        self.sign *= -1 if numer < 0 < denom or denom < 0 < numer else 1
        self.__numer, self.__denom = abs(numer), abs(denom)
        self._reduction()

    @staticmethod
    def _gcd(a, b):
        while b != 0:
            a, b = b, a % b
            if b == 0:
                return a

    def _single_denominator(self, other) -> tuple[int, int, int]:
        gcd = self._gcd(self.__denom, other.__denom)
        n1 = int(self.__numer * other.__denom / gcd)
        n2 = int(other.__numer * self.__denom / gcd)
        d = int(self.__denom * other.__denom / gcd)
        return n1, n2, d

    def _addition(self, other, method: str):
        func = getattr(operator, method)
        numer1, numer2, denom = self._single_denominator(other)
        res = func(self.sign * numer1, other.sign * numer2)
        return abs(res), denom, -1 if res < 0 else 1

    def _multiply(self, o, flip=False):
        on, od = (o.__denom, o.__numer) if flip else (o.__numer, o.__denom)
        return (
            self.__numer * on,
            self.__denom * od,
            self.sign * o.sign
        )

    def __add__(self, other):
        n, d, s = self._addition(other, "add")
        return Fraction(n * s, d)

    def __sub__(self, other):
        n, d, s = self._addition(other, "sub")
        return Fraction(n * s, d)

    def __iadd__(self, other):
        self.__numer, self.__denom, self.sign = self._addition(other, "add")
        self._reduction()
        return self

    def __isub__(self, other):
        self.__numer, self.__denom, self.sign = self._addition(other, "sub")
        self._reduction()
        return self

    def __mul__(self, other):
        n, d, s = self._multiply(other)
        return Fraction(n * s, d)

    def __imul__(self, other):
        self.__numer, self.__denom, self.sign = self._multiply(other)
        self._reduction()
        return self

    def __truediv__(self, other):
        n, d, s = self._multiply(other, flip=True)
        return Fraction(n * s, d)

    def __itruediv__(self, other):
        self.__numer, self.__denom, self.sign = self._multiply(other, flip=True)
        self._reduction()
        return self

    def __eq__(self, other):
        return self.__numer == other.__numer and self.__denom == other.__denom

    def __lt__(self, other):
        n1, n2, _ = self._single_denominator(other)
        return self.sign * n1 < other.sign * n2

    def __gt__(self, other):
        n1, n2, _ = self._single_denominator(other)
        return self.sign * n1 > other.sign * n2

    def __le__(self, other):
        n1, n2, _ = self._single_denominator(other)
        return self.sign * n1 <= other.sign * n2

    def __ge__(self, other):
        n1, n2, _ = self._single_denominator(other)
        return self.sign * n1 >= other.sign * n2

    def __ne__(self, other):
        n1, n2, _ = self._single_denominator(other)
        return self.sign * n1 != other.sign * n2

    def __neg__(self):
        sign = "-" if self.sign * (-1) == -1 else ""
        val = f'{sign}{str(self.__numer)}/{str(self.__denom)}'
        return Fraction(val)

    def _reduction(self):
        gcd = self._gcd(self.__numer, self.__denom)
        if gcd is not None:
            self.__denom = int(self.__denom / gcd)
            self.__numer = int(self.__numer / gcd)

    def numerator(self, number=None):
        if number is not None:
            self.sign *= -1 if number < 0 else 1
            self.__numer = abs(number)
            self._reduction()
        return self.__numer

    def denominator(self, number=None):
        if number is not None:
            self.sign *= -1 if number < 0 else 1
            self.__denom = abs(number)
            self._reduction()

        return self.__denom

    def reverse(self):
        return Fraction(self.__denom * self.sign, self.__numer)

    def __str__(self):
        sign = "-" if self.sign == -1 else ""
        return sign + str(self.__numer) + '/' + str(self.__denom)

    def __repr__(self):
        sign = "-" if self.sign == -1 else ""
        return (
                self.__class__.__name__
                + f"('{sign}{str(self.__numer)}/{str(self.__denom)}')"
        )


if __name__ == '__main__':
    a = Fraction(1, 3)
    b = Fraction(1, 2)
    print(a > b, a < b, a >= b, a <= b, a == b, a >= b)

    a = Fraction(1, 3)
    b = Fraction(6, 2).reverse()
    print(a > b, a < b, a >= b, a <= b, a == b, a >= b)