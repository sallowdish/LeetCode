class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        globalMaxLength = 0
        startPoint = 0
        endPoint = 0
        for i in range(len(s)):
            for j in range(len(s), i, -1):
                subString = s[i:j]
                if subString == subString[::-1]:
                    if len(subString) > globalMaxLength:
                        startPoint = i
                        endPoint = j
                        globalMaxLength = len(subString)
                        break
        return s[startPoint: endPoint]