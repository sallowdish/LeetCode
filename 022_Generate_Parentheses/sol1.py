class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        pList = [[""]]
        for i in range(n):
            newParenthesis = []
            for s in pList[i]:
                newParenthesis += self.insertParenthesis(s)
            pList.append(list(set(newParenthesis)))
        return pList[-1]

    def insertParenthesis(self, s):
        l = []
        for i in range(int(len(s) / 2) + 1):
            l.append(s[:i] + "()" + s[i:])
        return l
