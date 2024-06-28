import operator


class Fraction:
    def __init__(self, numer: str | int, denom: int | None = None):
        self.sign = 1
        if isinstance(numer, str):
            numer, denom = map(int, numer.split('/'))

        self.sign *= -1 if numer < 0 < denom or denom < 0 < numer else 1
        self.numer, self.denom = abs(numer), abs(denom)
        self._reduction()

    def _calculate(self, other, method: str):
        func = getattr(operator, method)
        gcd = self._gcd(self.denom, other.denom)
        numer1 = int(self.numer * other.denom / gcd)
        numer2 = int(other.numer * self.denom / gcd)
        res = func(self.sign * numer1, other.sign * numer2)
        sign = -1 if res < 0 else 1
        return abs(res), int(self.denom * other.denom / gcd), sign

    def __add__(self, other):
        n, d, s = self._calculate(other, "add")
        return Fraction(n * s, d)

    def __sub__(self, other):
        n, d, s = self._calculate(other, "sub")
        return Fraction(n * s, d)

    def __iadd__(self, other):
        self.numer, self.denom, self.sign = self._calculate(other, "add")
        self._reduction()
        return self

    def __isub__(self, other):
        self.numer, self.denom, self.sign = self._calculate(other, "sub")
        self._reduction()
        return self

    def __neg__(self):
        sign = "-" if self.sign * (-1) == -1 else ""
        val = f'{sign}{str(self.numer)}/{str(self.denom)}'
        return Fraction(val)

    @staticmethod
    def _gcd(a, b):
        while b != 0:
            a, b = b, a % b
            if b == 0:
                return a

    def _reduction(self):
        gcd = self._gcd(self.numer, self.denom)
        if gcd is not None:
            self.denom = int(self.denom / gcd)
            self.numer = int(self.numer / gcd)

    def numerator(self, number=None):
        if number is not None:
            self.sign *= -1 if number < 0 else 1
            self.numer = abs(number)
            self._reduction()
        return self.numer

    def denominator(self, number=None):
        if number is not None:
            self.sign *= -1 if number < 0 else 1
            self.denom = abs(number)
            self._reduction()

        return self.denom

    def __str__(self):
        sign = "-" if self.sign == -1 else ""
        return sign + str(self.numer) + '/' + str(self.denom)

    def __repr__(self):
        sign = "-" if self.sign == -1 else ""
        return (
                self.__class__.__name__
                + f"('{sign}{str(self.numer)}/{str(self.denom)}')"
        )


if __name__ == '__main__':
    a = Fraction(1, 3)
    b = Fraction(1, 2)
    c = a + b
    print(a, b, c, a is c, b is c)

    a = Fraction(1, 8)
    c = b = Fraction(3, 8)
    b -= a
    print(a, b, c, b is c)
