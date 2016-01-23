class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        import re
        s = "".join(re.findall("[\w]+", s)).lower()
        return s == s[::-1]