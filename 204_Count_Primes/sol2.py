import math


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        candidates = [0, 0] + [1 for x in range(2, n)]
        for i in range(2, int(math.sqrt(n)) + 1):
            if candidates[i] and self.isPrime(i):
                k = i
                while i*k < n:
                    candidates[i*k] = 0
                    k += 1
        return candidates.count(1)

    def isPrime(self, n):
        upper_bound = int(math.sqrt(n)) + 1
        for i in range(2, upper_bound):
            if n % i == 0:
                return False
        return True
