class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        sum = 0
        for d in str(num):
            sum += int(d)
            if not sum < 10:
                sum = sum / 10 + sum % 10
        return sum
