class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        upperBound = 2147483647
        isNeg = 1 if x < 0 else 0
        s = str(abs(x))
        reval = 0 if long(s[::-1]) > upperBound else int(s[::-1])
        return -reval if isNeg else reval