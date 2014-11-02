__author__ = 'Darryl'

from fractions import gcd


class Fraction:
    def __init__(self, num, denom):
        if isinstance(num, int) and isinstance(denom, int):
            common = gcd(num, denom)
            self._num = num//common
            self._denom = denom//common
        else:
            raise TypeError

    def __str__(self):
        return "%d / %d" % (self._num, self._denom)

    def __repr__(self):
        return '%s, In percentages: %d%%' % (str(self), self._num / self._denom * 100)

    def __add__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        denum = (self._num * other.get_denom()) + (other.get_num() * self._denom)
        div = (self._denom * other.get_denom())
        return Fraction(denum, div)
    __radd__ = __add__

    def __iadd__(self, other):
        return self + other

    def __sub__(self, other):
        denum = (self._num * other.get_denom()) - (other.get_num() * self._denom)
        div = (self._denom * other.get_denom())
        return Fraction(denum, div)

    def __mul__(self, other):
        denum = self._num * other.get_num()
        div = self._denom * other.get_denom()
        return Fraction(denum, div)

    def __truediv__(self, other):
        temp_fraction = Fraction(other.get_denom(), other.get_num())
        return self.__mul__(temp_fraction)

    def eq_denom(self, other):
        first = self._num * other.get_denom()
        last = other.get_num() * self._denom
        return first, last

    def __eq__(self, other):
        first, last = self.eq_denom(other)
        return first == last

    def __ne__(self, other):
        first, last = self.eq_denom(other)
        return first != last

    def __gt__(self, other):
        first, last = self.eq_denom(other)
        return first > last

    def __ge__(self, other):
        first, last = self.eq_denom(other)
        return first >= last

    def __lt__(self, other):
        first, last = self.eq_denom(other)
        return first < last

    def __le__(self, other):
        first, last = self.eq_denom(other)
        return first <= last

    def get_num(self):
        return self._num

    def get_denom(self):
        return self._denom


def main():
    """
    Checking if instantiating a fraction works
    >>> print(Fraction(1, 2))
    1 / 2
    >>> print(Fraction(-1, 2))
    -1 / 2
    >>> print(Fraction('Foo', 'Bar'))
    Traceback (most recent call last):
    TypeError
    >>> Fraction(1, 2)
    1 / 2, In percentages: 50%

    Adding a fraction to another fraction
    >>> print(Fraction(1, 2) + Fraction(1, 4))
    3 / 4
    >>> print(Fraction(-1, 2) + Fraction(2, 2))
    1 / 2
    >>> print(Fraction(-1, 5) + Fraction(-1, 5))
    -2 / 5
    >>> print(Fraction(-1, -5) + Fraction(-1, -5))
    2 / 5
    >>> f1 = Fraction(1, 2)
    >>> f1 += Fraction(1, 4)
    >>> print(f1)
    3 / 4

    Adding a fraction to an integer
    >>> print(Fraction(1, 2) + 1)
    3 / 2
    >>> print(2 + Fraction(1, 2))
    5 / 2
    >>> f1 = Fraction(1, 2)
    >>> f1 += 1
    >>> print(f1)
    3 / 2

    Substracting a fraction from another
    >>> print(Fraction(3, 4) - Fraction(1, 4))
    1 / 2
    >>> print(Fraction(-1, 2) - Fraction(1, 4))
    -3 / 4
    >>> print(Fraction(-2, 10) - Fraction(-1, 10))
    -1 / 10
    >>> print(Fraction(-2, -10) - Fraction(-1, -10))
    1 / 10

    Multiplying 2 fractions
    >>> print(Fraction(1, 5) * Fraction(1, 2))
    1 / 10
    >>> print(Fraction(-1, 2) * Fraction(1, 4))
    -1 / 8
    >>> print(Fraction(-1, 2) * Fraction(-1, 8))
    1 / 16
    >>> print(Fraction(-1, -2) * Fraction(-1, -8))
    1 / 16

    Dividing 2 fractions
    >>> print(Fraction(1, 4) / Fraction(1, 2))
    1 / 2
    >>> print(Fraction(-1, 2) / Fraction(1, 15))
    -15 / 2
    >>> print(Fraction(-4, 5) / Fraction(-1, 2))
    8 / 5
    >>> print(Fraction(-4, -5) / Fraction(-1, -2))
    8 / 5

    Equality between fractions
    >>> print(Fraction(1, 2) == Fraction(2, 4))
    True
    >>> print(Fraction(1, 2) == Fraction(1, 3))
    False
    >>> print(Fraction(-2, 4) == Fraction(-1, 2))
    True
    >>> print(Fraction(-2, -4) == Fraction(-1, -2))
    True

    Non-equality between fractions
    >>> print(Fraction(1, 2) != Fraction(64, 128))
    False
    >>> print(Fraction(1, 4) != Fraction(999, 4000))
    True
    >>> print(Fraction(-3, 4) != Fraction(-3, 5))
    True
    >>> print(Fraction(-3, -4) != Fraction(-3, -5))
    True

    Larger size difference between fractions
    >>> print(Fraction(1, 2) > Fraction(857, 1713))
    False
    >>> print(Fraction(1, 2) > Fraction(857, 1715))
    True
    >>> print(Fraction(1, 338) >= Fraction(2, 676))
    True
    >>> print(Fraction(-2, 5) > Fraction(-1, 5))
    False
    >>> print(Fraction(-2, -5) > Fraction(-1, -5))
    True

    Smaller size difference between fractions
    >>> print(Fraction(1, 2) < Fraction(857, 1713))
    True
    >>> print(Fraction(1, 2) < Fraction(857, 1715))
    False
    >>> print(Fraction(1, 338) <= Fraction(2, 676))
    True
    >>> print(Fraction(-3, 7) < Fraction(-6, 7))
    False
    >>> print(Fraction(-3, -7) < Fraction(-6, -7))
    True
    """
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    main()