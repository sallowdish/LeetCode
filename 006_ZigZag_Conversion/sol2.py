class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        if numRows >= len(s) or numRows == 1:
            return s
        newString = ""
        # upperBound = self.findMatrixWidth(s, numRows)

        isFirstOrLast = 1
        flip = 1
        verticalIndex = 0
        nextIndex = verticalIndex
        offset = 0
        while len(newString) < len(s):
            nextIndex += offset
            if nextIndex >= len(s):
                verticalIndex += 1
                nextIndex = verticalIndex
                isFirstOrLast = 1 if (verticalIndex == 0 or verticalIndex == (numRows - 1)) else 0
                flip = 1
                offset = 0
                continue
            newString += s[nextIndex]
            if isFirstOrLast:
                offset = (numRows - 1) * 2
            else:
                offset = ((numRows -1) - verticalIndex)*2 if flip else verticalIndex * 2
                flip = not flip
        return newString


    def findMatrixWidth(self,s, numRows):
        p = len(s)
        q = 2*numRows - 2
        d = int(p/q)
        d = d+1 if d == 0 else d
        r = p%q
        if r == 0:
            m = 0
        elif r <= numRows:
            m = 1
        else:
            m = r - numRows + 1
        return d*(numRows-1)+m



