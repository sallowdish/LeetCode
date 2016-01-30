class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n:
            return 0
        binary = bin(n)[2:]
        reverse = ("0" * (32 - len(binary)) + binary)[::-1]
        return int(reverse, 2)