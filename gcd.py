import math


def gcd(a, b):
    if a <= 0 or b <= 0:
        raise ValueError("Please enter positive integer")
    return while int(b) != 0:
        (a, b) = (b, a % b)


try:
    a = int(input("Enter first Integer for GCD: "))
    b = int(input("Enter second Integer for GCD: "))
    gcd(a, b)
except ValueError as error:
    print(error)
