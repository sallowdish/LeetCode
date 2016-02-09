class SubString:
    s = ""
    start = end = 0

    def __init__(self, s, start, end):
        self.s = s
        self.start =start
        self.end = end

    def __eq__(self, other):
        return self.s == other.s

    def __str__(self):
        return self.s

class Solution:

    candidates = []

    def longestPalindrome(self, s):
        """
        Apriori algorithm
        :param s:
        :return:
        """
        globalMaxLength = 0
        globalMaxSubString = ""
        self.initCandidates(s)
        while len(self.candidates):
            c = self.candidates.pop()
            if len(c[0]) > globalMaxLength:
                globalMaxLength = len(c[0])
                globalMaxSubString = c[0]
            self.tryExpandCandidates(s, c, globalMaxLength)
        return globalMaxSubString


    def initCandidates(self, s):
        newList = []
        if len(s) <= 1:
            newList.append((s,0,1))
        elif len(s) == 2:
            if s == s[::-1]:
                newList.append((s,0,2))
            else:
                newList.append((s[0],0,1))
        else:
            for i in range(len(s) - 1):
                subString = s[i:i+2]
                if subString == subString[::-1]:
                    newList.append((subString, i, i+2))
            for i in range(len(s) - 2):
                subString = s[i:i+3]
                if subString == subString[::-1]:
                    newList.append((subString, i, i+3))
        self.candidates = newList

    def tryExpandCandidates(self, s, c, globalMaxLength):
        armLength = int((globalMaxLength - len(c[0]))/2)+1
        newStart = 0 if c[1] - armLength < 0 else c[1] - armLength
        newEnd = len(s) if c[2] + armLength > len(s) else c[2] + armLength
        newSubString = s[newStart: newEnd]
        if len(newSubString) > globalMaxLength and newSubString == newSubString[::-1]:
            self.candidates.append((newSubString, newStart, newEnd))
        return