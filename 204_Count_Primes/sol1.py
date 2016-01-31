import math


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        candidates = list(range(2, n))
        factor = [2] + list(range(3, int(math.sqrt(n)) + 1, 2))
        for f in factor:
            candidates = [c for c in candidates if (c == f or c % f != 0)]
        return len(candidates)
