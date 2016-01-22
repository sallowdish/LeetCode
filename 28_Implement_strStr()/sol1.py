class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if haystack == needle:
            return 0
        l = len(needle)
        countDict = {}
        for i in range(len(haystack) - l + 1):
            subString = haystack[i:i+l]
            if subString not in countDict:
                countDict[subString] = i
        if needle in countDict:
            return countDict[needle]
        else:
            return -1