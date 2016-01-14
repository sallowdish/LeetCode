class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        globalMaxSubString = ""
        localSubString = ""
        i = 0
        for j in range(len(s)):
            char = s[j]
            if char in localSubString:
                if len(localSubString) > len(globalMaxSubString):
                    globalMaxSubString = localSubString
                i = i + list(localSubString).index(char) + 1
                localSubString = s[i:j]
            localSubString += char
        if len(localSubString) > len(globalMaxSubString):
            globalMaxSubString = localSubString
        return len(globalMaxSubString)