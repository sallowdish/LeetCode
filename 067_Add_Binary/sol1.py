class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if not a:
            return b
        if not b:
            return a
        ret = ""
        if len(a) < len(b):
            a, b = b, a
        carrier = index = 0
        while index < len(a):
            if index < len(b):
                sum = int(a[-index - 1]) + int(b[-index - 1]) + carrier
            else:
                sum = int(a[-index - 1]) + carrier
            carrier = 1 if sum > 1 else 0
            sum %= 2
            ret = str(sum) + ret
            index += 1
        if carrier:
            ret = "1" + ret
        return ret
