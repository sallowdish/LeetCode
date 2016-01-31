class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        return len(list(primes_sieve2(n )))


def sieve(n):
    "Return all primes <= n."
    np1 = n + 1
    s = list(range(np1))  # leave off `list()` in Python 2
    s[1] = 0
    sqrtn = int(round(n ** 0.5))
    for i in range(2, sqrtn + 1):  # use `xrange()` in Python 2
        if s[i]:
            # next line:  use `xrange()` in Python 2
            s[i * i: np1: i] = [0] * len(range(i * i, np1, i))
    return filter(None, s)

def primes_sieve2(limit):
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, i):     # Mark factors non-prime
                a[n] = False