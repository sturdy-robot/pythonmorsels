import decimal
import math


def is_perfect_square(number: int, complex=False):
    if number < 0 and complex is False or decimal.Decimal(number).is_nan():
        return False

    return math.sqrt(number).is_integer()