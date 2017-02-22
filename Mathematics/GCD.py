# Basic eucledian algorithm to find the greatest common divisor of 2 numbers


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

print(gcd(10, 15))
