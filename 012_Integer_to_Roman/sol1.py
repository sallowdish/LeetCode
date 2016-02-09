class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        reval = ""
        M = num / 1000
        reval += "M" * M
        r = num % 1000

        C = r / 100
        r = r % 100

        reval += self.constructSubString("C", "D", "M", C)

        X = r / 10
        r = r % 10
        reval += self.constructSubString("X", "L", "C", X)

        reval += self.constructSubString("I", "V", "X", r)

        return reval

    def constructSubString(self, s1, s2, s3, v):
        if v <= 3:
            return s1 * v
        elif v == 4:
            return s1 + s2
        elif v <= 8:
            return s2 + s1 * (v - 5)
        else:
            return s1 + s3
