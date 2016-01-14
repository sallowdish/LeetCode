class Solution:
    """
    BFS
    """
    checkedString = {}

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        return self.searchPalindrome(s)

    def searchPalindrome(self, s):
        toSearch = [s]
        while len(toSearch) > 0:
            subString = toSearch.pop()
            if subString not in self.checkedString:
                if len(subString) <=1:
                    return subString
                if subString == subString[::-1]:
                    return subString
                # subString is not a palidrome
                self.checkedString[subString] = 0
                toSearch.insert(0, subString[1:])
                toSearch.insert(0, subString[:-1])