class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        n = len(obstacleGrid[0])
        m = len(obstacleGrid)
        if not n or not m:
            return 0
        matrix = [[0 for i in xrange(n)] for j in xrange(m)]
        # print matrix
        for i in xrange(m):
            for j in xrange(n):
                if obstacleGrid[i][j] == 1:
                    matrix[i][j] = 0
                else:
                    if i == 0 and j == 0:
                        matrix[i][j] = 1
                        continue
                    # first row
                    if i == 0:
                        matrix[i][j] = matrix[i][j - 1]
                    # first col
                    elif j == 0:
                        matrix[i][j] = matrix[i - 1][j]
                    # intermediate node
                    else:
                        matrix[i][j] = matrix[i][j - 1] + matrix[i - 1][j]
                # print matrix
        return matrix[-1][-1]

