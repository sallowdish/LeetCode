import re
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        upperBound = 2147483647
        s = str.strip()
        if s == "":
            return 0
        if re.match("^-{0,1}\d*$", s):
            long = int(s)
            if long > upperBound:
                return 0
            else:
                return long
        else:
            return 0