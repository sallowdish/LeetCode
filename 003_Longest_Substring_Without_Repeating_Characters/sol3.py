class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        countMap = {}
        globalMax = localCount = 0
        for i in s:
            if i not in countMap:
                localCount += 1
            else:
                globalMax = localCount if localCount > globalMax else globalMax

        return len(globalMaxSubString)