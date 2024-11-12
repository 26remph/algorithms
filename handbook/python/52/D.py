class Fraction:
    def __init__(self, numer: str | int, denom: str | int | None = None):
        if denom:
            self.numer, self.denom = int(numer), int(denom)
        else:
            self.numer, self.denom = map(int, numer.split("/"))
        self._reduction()

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
            self.numer = number
            self._reduction()
        return self.numer

    def denominator(self, number=None):
        if number is not None:
            self.denom = number
            self._reduction()

        return self.denom

    def __str__(self):
        return str(self.numer) + "/" + str(self.denom)

    def __repr__(self):
        return self.__class__.__name__ + f"({str(self.numer)}, {str(self.denom)})"


if __name__ == "__main__":
    fraction = Fraction(3, 9)
    print(fraction, repr(fraction))
    fraction = Fraction("7/14")
    print(fraction, repr(fraction))

    fraction = Fraction(3, 210)
    print(fraction, repr(fraction))
    fraction.numerator(10)
    print(fraction.numerator(), fraction.denominator())
    fraction.denominator(2)
    print(fraction.numerator(), fraction.denominator())
