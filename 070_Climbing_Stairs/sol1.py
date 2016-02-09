class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <3:
            return n
        return self.shiftedFib2(n)

    def shiftedFib(self, n):
        l = [1,2]
        for i in range(n - 2):
            l.append(l[i] + l[i+1])
        return l

    def shiftedFib2(self, n):
        phi = (5**0.5 + 1)/2
        return round((phi**(n+2))/(phi+2))