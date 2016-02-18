class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        ret = []
        if len(num1) < len(num2):
            num1, num2 = num2, num1
        for i in range(len(num1)):
            for j in range(len(num2)):
                s = int(num1[i]) * int(num2[j])
                c1 = s//10
                c2 = s%10
                c1_index = i+j
                c2_index = i+j+1
                if c1_index == len(ret):
                    ret.append(c1)
                    ret.append(c2)
                elif c1_index == len(ret) - 1:
                    ret[c1_index] += c1
                    ret.append(c2)
                else:
                    ret[c1_index] += c1
                    ret[c2_index] += c2
        s = ""
        carrier = 0
        for i in ret[::-1]:
            n = i + carrier
            carrier = 0
            if n > 9:
                carrier = n //10
                n = n % 10
            s = str(n) + s
        return self.stripZore(s)

    def stripZore(self, s):
        index = 0
        while index < len(s) and s[index] == "0":
            index += 1
        s = s[index:]
        return "0" if not s else s