class Solution(object):
    directions = ('right', 'down', 'left', 'up')
    round = 0

    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        if len(matrix) == 1:
            return matrix[0]
        if len(matrix[0]) == 1:
            return [x[0] for x in matrix]
        else:
            m = len(matrix)
            n = len(matrix[0])
            ret = [matrix[0][0]]
            step = (0, 0, 'right')
            for i in range(m * n - 1):
                next_step = self.get_next_step(step[0], step[1], step[2], m, n)
                ret.append(matrix[next_step[0]][next_step[1]])
                step = next_step
        return ret

    def get_next_step(self, i, j, dir, m, n):
        if dir == self.directions[0]:
            if j + 1 < n - self.round - 1:
                return (i, j + 1, dir)
            else:
                return (i, j + 1, self.directions[1])
        elif dir == self.directions[1]:
            if i + 1 < m - 1 - self.round:
                return (i + 1, j, dir)
            else:
                return (i + 1, j, self.directions[2])
        elif dir == self.directions[2]:
            if j - 1 > self.round:
                return (i, j - 1, dir)
            else:
                return (i, j - 1, self.directions[3])
        elif dir == self.directions[3]:
            if i - 1 > self.round + 1:
                return (i - 1, j, dir)
            else:
                self.round += 1
                return (i - 1, j, self.directions[0])
