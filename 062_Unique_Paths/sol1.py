class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        matrix = [[1 for i in xrange(n)] if j==0 else [1 if i ==0 else 0 for i in xrange(n)]for j in xrange(m)]
        for i in range(1, m):
            for j in range(1, n):
                # print (i,j)
                matrix[i][j] = matrix[i-1][j] + matrix[i][j - 1]
        return matrix[-1][-1]
