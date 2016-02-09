class Solution:
    """
    BFS
    """
    def longestPalindrome(self, s):
        globalMaxLength = 0
        globalMaxSubString = ""

        for i in range(len(s)):
            for j in range(globalMaxLength, i+1):
                subString = s[i-j:i+j+1]
                if subString == subString[::-1]:
                    if len(subString) > globalMaxLength:
                        globalMaxLength = int((len(subString))/2)+1
                        globalMaxSubString = subString
        return globalMaxSubString