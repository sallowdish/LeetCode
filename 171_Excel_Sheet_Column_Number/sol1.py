class Solution(object):

    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum = 0
        weight = 0
        for d in s[::-1]:
            value = ord(d) - 64
            sum += value * (26 ** weight)
            weight += 1
        return sum