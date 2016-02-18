class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        l = []
        count = 0
        if len(num1) < len(num2):
            num1, num2 = num2, num1
        for i in num2[::-1]:
            l.append(self.multiplyStrWithDigit(num1, int(i)) + "0" * count)
            count += 1
        return self.stripZore(self.sumListOfStr(l))

    def multiplyStrWithDigit(self, s, d):
        if d == 0:
            return "0"
        if d == 1:
            return s
        if not 0 < d < 10:
            raise ValueError
        ret = ""
        carrier = 0
        for i in s[::-1]:
            p = int(i) * d + carrier
            ret = str(p % 10) + ret
            carrier = p // 10
        if carrier:
            ret = str(carrier) + ret
        return ret

    def addTwoStr(self, s1, s2):
        if s1 == "0":
            return s2
        if s2 == "0":
            return s1
        sum = ""
        if len(s1) != len(s2):
            diff = len(s1) - len(s2)
            if diff < 0:
                s1 = diff * "0" + s1
            else:
                s2 = diff * "0" + s2
        carrier = 0
        for i in range(1, len(s1)+1):
            d1 = int(s1[-i])
            d2 = int(s2[-i])
            s = d1 + d2 + carrier
            if s >= 10:
                carrier = 1
                s %= 10
            else:
                carrier = 0
            sum = str(s) + sum
        if carrier:
            sum = "1" + sum
        return sum

    def sumListOfStr(self, l):
        if not l:
            return ""
        sum = max([len(x) for x in l]) * "0"
        for s in l:
            sum = self.addTwoStr(sum, s)
        return sum

    def stripZore(self, s):
        index = 0
        while index < len(s) and s[index] == "0":
            index += 1
        s = s[index:]
        return "0" if not s else s
