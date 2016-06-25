class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            raise ValueError('x must be non-negtive')
        if x == 0:
            return 0
        i = 0
        while (2 ** i) ** 2 < x:
            i += 1
        if (2 ** i) ** 2 == x:
            return 2 ** i
        else:
            # root between 2^(i -1) and 2^i
            return self.binary_search(2 ** (i - 1), 2 ** i, x)

    def binary_search(self, start, end, x):
        if start == end:
            raise IndexError("can't find target value")
        if start + 1 == end:
            return start
        mid = (start + end) // 2
        if mid ** 2 == x:
            return mid
        elif mid ** 2 < x:
            return self.binary_search(mid, end, x)
        else:
            return self.binary_search(start, mid, x)
