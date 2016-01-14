class Solution(object):
    unitValue = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500,"M":1000}
    orderdUnit = ["M","D","C","L","X","V","I"]
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        reval = 0
        lastIndex = -1
        for unit in self.orderdUnit:
            try:
                localLast = s.rindex(unit)
            except:
                localLast = -1

            if localLast > lastIndex:
                subString = s[lastIndex+1:localLast+1]
                lastIndex = localLast
                reval += self.toInt(subString, unit)

        return reval

    def toInt(self, s, c1):
        val = 0
        v1 = self.unitValue[c1]
        for c in s:
            if c == c1:
                val += v1
            else:
                val -= self.unitValue[c]
        return val

