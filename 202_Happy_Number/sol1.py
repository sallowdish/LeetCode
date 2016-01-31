class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        visited_number = [n]
        while 1:
            digit = [int(d) for d in list(str(n))]
            n = sum([d**2 for d in digit])
            if n == 1:
                return True
            if n in visited_number:
                return False
            visited_number.append(n)