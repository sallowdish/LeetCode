import re
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        matchList = re.findall("\w+", s)

        return 0 if len(matchList) == 0 else len(matchList[-1])