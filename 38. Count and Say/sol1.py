class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        sayList = ["1"]
        for i in range(n - 1):
            sayList.append(self.strToSay(sayList[i]))
        return sayList[-1]

    def strToSay(self, s):
        l = []
        say = ""
        for i in range(len(s) - 1):
            if s[i] != s[i+1]:
               say += str(len(l) + 1) + s[i]
               l.clear()
            else:
                l.append(s[i])
        if len(l) == 0:
            say += "1" + s[-1]
        else:
            say +=  str(len(l) + 1) + s[-1]
        return say