import math


class Rational:
    def __init__(self, numerator=1, denominator=1):
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError('numerator and denominator must be an integer type')
        if denominator == 0:
            raise ZeroDivisionError("Can not divide by zero")
        self.__numerator = numerator
        self.__denominator = denominator

    def __str__(self):
        gcd = math.gcd(self.__numerator, self.__denominator)
        return f"{self.__numerator // gcd} / {self.__denominator // gcd}"

    def float_rational(self):
        return self.__numerator / self.__denominator

    def __add__(self, other):
        if not isinstance(other, Rational):
            raise TypeError(f"Unsupported operand type for {type(self.__name__)} and {type(other.__name__)}")
        common_denominator = math.lcm(self.__denominator, other.__denominator)
        return Rational(common_denominator // self.__denominator * self.__numerator + common_denominator //
                        other.__denominator * other.__numerator, common_denominator)

    def __sub__(self, other):
        if not isinstance(other, Rational):
            raise TypeError(f"Unsupported operand type for {type(self.__name__)} and {type(other.__name__)}")
        common_denominator = math.lcm(self.__denominator, other.__denominator)
        return Rational(common_denominator // self.__denominator * self.__numerator - common_denominator //
                        other.__denominator * other.__numerator, common_denominator)

    def __mul__(self, other):
        if not isinstance(other, Rational):
            raise TypeError(f"Unsupported operand type for {type(self.__name__)} and {type(other.__name__)}")
        return Rational(self.__numerator * other.__numerator, self.__denominator * other.__denominator)

    def __floordiv__(self, other):
        if not isinstance(other, Rational):
            raise TypeError(f"Unsupported operand type for {type(self.__name__)} and {type(other.__name__)}")
        return Rational(self.__numerator * other.__denominator, self.__denominator * other.__numerator)

    def __gt__(self, other):
        if not isinstance(other, Rational):
            raise TypeError(f"Unsupported operand type for {type(self.__name__)} and {type(other.__name__)}")
        return self.float_rational() > other.float_rational()

    def __lt__(self, other):
        if not isinstance(other, Rational):
            raise TypeError(f"Unsupported operand type for {type(self.__name__)} and {type(other.__name__)}")
        return self.float_rational() < other.float_rational()

    def __ge__(self, other):
        if not isinstance(other, Rational):
            raise TypeError(f"Unsupported operand type for {type(self.__name__)} and {type(other.__name__)}")
        return self.float_rational() >= other.float_rational()

    def __le__(self, other):
        if not isinstance(other, Rational):
            raise TypeError(f"Unsupported operand type for {type(self.__name__)} and {type(other.__name__)}")
        return self.float_rational() <= other.float_rational()

    def __eq__(self, other):
        if not isinstance(other, Rational):
            raise TypeError(f"Unsupported operand type for {type(self.__name__)} and {type(other.__name__)}")
        return self.float_rational() == other.float_rational()

    def __ne__(self, other):
        if not isinstance(other, Rational):
            raise TypeError(f"Unsupported operand type for {type(self.__name__)} and {type(other.__name__)}")
        return self.float_rational() != other.float_rational()


a = Rational(1, 4)
b = Rational(1, 2)
print(b - a)

