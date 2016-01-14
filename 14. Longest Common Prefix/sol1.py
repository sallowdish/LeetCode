class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        currentIndex = 0
        commonPrefix = ""
        countDict = {}
        while(1):
            for s in strs:
                if currentIndex < len(s):
                    c = s[currentIndex]
                    if c in countDict:
                        countDict[c] += 1
                    else:
                        countDict[c] = 1
                else:
                    return commonPrefix
            if len(countDict) == 0:
                return commonPrefix
            commonChar = max(countDict, key=lambda x: countDict[x])
            if countDict[commonChar] < len(strs):
                return commonPrefix
            else:
                commonPrefix += commonChar
            strs = [s for s in strs if s[currentIndex] == commonChar]
            countDict.clear()
            currentIndex += 1

        return commonPrefix