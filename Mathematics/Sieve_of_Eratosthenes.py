# Given a number n, print all primes smaller than or equal to n. It is also given that n is a small number.
""" The sieve of Eratosthenes is one of the most efficient ways to find all primes smaller than n when n is
smaller than 10 million or so """


# function to find prime numbers less than or equal to num
def find_primes_sieve(num):
    # list of all numbers upto n
    intList = [True for i in range(num+1)]

    # first prime
    p = 2

    while p * p <= num:

        # if intList[p] is True means its a prime number
        if intList[p]:
            for i in range(p**2, num+1, p):
                intList[i] = False

        p += 1

    lis = []
    for i in range(2, len(intList)):
        if intList[i]:
            lis.append(i)

    return lis

if __name__ == '__main__':
    primes = find_primes_sieve(30)
    print(primes)