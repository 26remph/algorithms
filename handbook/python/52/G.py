import operator
import random

from check_g import Fraction as CheckFraction


class Fraction:
    def __init__(self, numer: str | int, denom: int | None = None):
        self.sign = 1
        if isinstance(numer, str):
            numer, denom = map(int, numer.split("/"))

        self.sign *= -1 if numer < 0 < denom or denom < 0 < numer else 1
        self.__numer, self.__denom = abs(numer), abs(denom)
        self._reduction()

    def _calculate(self, other, method: str):
        func = getattr(operator, method)
        gcd = self._gcd(self.__denom, other.__denom)
        numer1 = int(self.__numer * other.__denom / gcd)
        numer2 = int(other.__numer * self.__denom / gcd)
        res = func(self.sign * numer1, other.sign * numer2)
        sign = -1 if res < 0 else 1
        return abs(res), int(self.__denom * other.__denom / gcd), sign

    def _multiply(self, other):
        return (
            self.__numer * other.__numer,
            self.__denom * other.__denom,
            self.sign * other.sign,
        )

    def _divide(self, other):
        return (
            self.__numer * other.__denom,
            self.__denom * other.__numer,
            self.sign * other.sign,
        )

    def __add__(self, other):
        n, d, s = self._calculate(other, "add")
        return Fraction(n * s, d)

    def __sub__(self, other):
        n, d, s = self._calculate(other, "sub")
        return Fraction(n * s, d)

    def __iadd__(self, other):
        self.__numer, self.__denom, self.sign = self._calculate(other, "add")
        self._reduction()
        return self

    def __isub__(self, other):
        self.__numer, self.__denom, self.sign = self._calculate(other, "sub")
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
        n, d, s = self._divide(other)
        return Fraction(n * s, d)

    def __itruediv__(self, other):
        self.__numer, self.__denom, self.sign = self._divide(other)
        self._reduction()
        return self

    def __neg__(self):
        sign = "-" if self.sign * (-1) == -1 else ""
        val = f"{sign}{str(self.__numer)}/{str(self.__denom)}"
        return Fraction(val)

    @staticmethod
    def _gcd(a, b):
        while b != 0:
            a, b = b, a % b
            if b == 0:
                return a

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
        return sign + str(self.__numer) + "/" + str(self.__denom)

    def __repr__(self):
        sign = "-" if self.sign == -1 else ""
        return (
            self.__class__.__name__
            + f"('{sign}{str(self.__numer)}/{str(self.__denom)}')"
        )


if __name__ == "__main__":
    n, d, k, m = [
        random.choice([x for x in range(-10, 10) if x != 0]) for _ in range(4)
    ]
    print(n, d, k, m)
    a = Fraction(n, d)
    a1 = CheckFraction(n, d)

    b = Fraction(k, m)
    b1 = CheckFraction(k, m)
    action = random.choice([operator.mul, operator.truediv])
    c = a * b
    c1 = a1 * b1
    print(a, b, c, a is c, b is c)
    print(a1, b1, c1, a1 is c1, b1 is c1)
    print(a.reverse().__str__() == a1.reverse().__str__())
    print(a.reverse().__str__())
    print(a1.reverse().__str__())

    assert a.__str__() == a1.__str__()
    assert b.__str__() == b1.__str__()
    assert c.__str__() == c1.__str__()
    assert a.reverse().__str__() == a1.reverse().__str__()
