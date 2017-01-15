# print all prime factors of a given number
"""Given a number n, write an efficient function to print all prime factors of n.
 For example, if the input number is 12, then output should be “2 2 3”."""

from math import sqrt

def prime_factors(num):
    # list to store the prime factors
    prime_factor_lis = []

    # if 2 is a factor of the number
    while num % 2 == 0:
        prime_factor_lis.append(2)
        num /= 2

    for i in range(3, int(sqrt(num)), 2):
        while num % i == 0:
            prime_factor_lis.append(i)
            num /= i

    return prime_factor_lis

if __name__ == '__main__':
    print(prime_factors(315))


