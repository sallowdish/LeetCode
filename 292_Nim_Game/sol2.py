class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1:
            raise ValueError()
        else:
            return n % 4 != 0
