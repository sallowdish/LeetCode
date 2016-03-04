class Solution(object):
    def minPathSum(self, grid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        n = len(grid[0])
        m = len(grid)
        if not n or not m:
            return 0
        matrix = [[0 for i in xrange(n)] for j in xrange(m)]
        # print matrix
        for i in xrange(m):
            for j in xrange(n):
                if i == 0 and j == 0:
                    matrix[i][j] = grid[i][j]
                    continue
                # first row
                if i == 0:
                    matrix[i][j] = matrix[i][j - 1] + grid[i][j]
                # first col
                elif j == 0:
                    matrix[i][j] = matrix[i - 1][j] + grid[i][j]
                # intermediate node
                else:
                    matrix[i][j] = min(matrix[i][j - 1], matrix[i - 1][j]) + \
                                   grid[i][j]
                # print matrix
        return matrix[-1][-1]

