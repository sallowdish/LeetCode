class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n:
            return 0
        binary = bin(n)[2:][::-1]
        reverse = binary +  "0" * (32 - len(binary))
        return int(reverse, 2)
