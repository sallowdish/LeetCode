class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        return self.searchPalindrome(s)

    def generateCandidates(self, s, size = 2):
        rev = []
        for i in range(len(s) - size + 1):
            rev.append(s[i:i+size])
        return set(rev)

    def searchPalindrome(self, s):
        if len(s) == 1:
            return s
        longestSubString = ""
        s1 = s
        s2 = s[::-1]
        for i in range(1,len(s)+1):
            candidates1 = self.generateCandidates(s1, i)
            candidates2 = self.generateCandidates(s2, i)
            intersection = candidates1.intersection(candidates2)
            if len(intersection) > 0 :
                longestSubString = intersection.pop()
            else:
                break
        return longestSubString

