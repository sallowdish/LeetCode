class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        globalMaxStartPoint = globalMaxEndPoint = globalMaxLength = 0
        i = 0
        for j in range(len(s)):
            subString = s[i:j]
            char = s[j]
            if char in subString:
                i = i + list(subString).index(char) + 1
            else:
                if len(subString) + 1 > globalMaxLength:
                    globalMaxStartPoint = i
                    globalMaxEndPoint = j + 1
                    globalMaxLength = len(subString) + 1
        #return s[globalMaxStartPoint:globalMaxEndPoint]
        return globalMaxEndPoint - globalMaxStartPoint