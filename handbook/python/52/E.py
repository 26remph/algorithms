class Fraction:
    def __init__(self, numer: str | int, denom: int | None = None):
        self.sign = 1
        if isinstance(numer, str):
            numer, denom = map(int, numer.split('/'))

        self.sign *= -1 if numer < 0 < denom or denom < 0 < numer else 1
        self.numer, self.denom = abs(numer), abs(denom)
        self._reduction()

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
    b = Fraction(-2, -6)
    c = Fraction(-3, 9)
    d = Fraction(4, -12)
    print(a, b, c, d)
    print(*map(repr, (a, b, c, d)))

    a = Fraction('-1/2')
    b = -a
    print(a, b, a is b)
    b.numerator(-b.numerator())
    a.denominator(-3)
    print(a, b)
    print(a.numerator(), a.denominator())
    print(b.numerator(), b.denominator())