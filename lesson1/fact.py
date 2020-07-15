import math
from decimal import Decimal


def fact(n):
    return n / (Decimal(math.factorial(n)) ** Decimal(1 / n))


epsilon = 10 ** -7

n = 2
while fact(n) - fact(n - 1) > epsilon:
    n = n + 10

print(fact(n))




