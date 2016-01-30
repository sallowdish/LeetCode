import math
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n:
            return 0
        upper_bound = math.log(n, 5)
        power = 1
        sum = 0
        while power <= upper_bound:
            sum += int(n/(5**power))
            power += 1
        return sum