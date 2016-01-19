class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carrier = 1
        for i in range(1, len(digits) + 1):
            d = digits[-i]
            sum = d + carrier
            if sum < 10:
                carrier = 0
                digits[-i] = sum
            else:
                digits[-i] = sum % 10
        if carrier:
            digits.insert(0, 1)
        return digits