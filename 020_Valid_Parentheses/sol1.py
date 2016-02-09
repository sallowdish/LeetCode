class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lastUnmatch = -1
        left =["(","[","{"]
        l = []
        for i in xrange(len(s)):
            c = s[i]
            if c in left:
                l.append(lastUnmatch)
                lastUnmatch=i
            else:
                cBar = s[lastUnmatch]
                if self.match(c, cBar):
                    lastUnmatch = l.pop()
                else:
                    return False
        return lastUnmatch == -1
    
    def match(self,c1, c2):
        if c1 == ")":
            return c2 =="("
        elif c1 == "]":
            return c2 == "["
        elif c1 == "}":
            return c2 == "{"
        else:
            return 0