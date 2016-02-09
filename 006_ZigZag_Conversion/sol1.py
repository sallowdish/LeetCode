class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s
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

        matrix = [["" for x in range(d*(numRows-1)+m)] for y in range(numRows)]

        self.fillMatrix(matrix, s)

        return "".join(["".join(x) for x in matrix])

    def fillMatrix(self, matrix, s):
        i = j = 0
        isZig = 1
        for c in s:
            matrix[i][j] = c
            if isZig:
                if i + 1 < len(matrix):
                    i += 1
                else:
                    i -= 1
                    if i > 0:
                        isZig = 0
                    j += 1
            else:
                j += 1
                i -= 1
                if i == 0:
                    isZig = 1


