class Solution(object):
    directions = ('right', 'down', 'left', 'up')
    round = 0

    def generateMatrix(self, n):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if n < 0:
            raise ValueError("n has to be non-negtive.")
        if n == 0:
            return [[]]
        ret = [[0 for i in range(n)] for j in range(n)]
        step = (0, 0, 'right')
        for i in range(1, n ** 2 + 1):
            ret[step[0]][step[1]] = i
            next_step = self.get_next_step(step[0], step[1], step[2], n, n)
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
