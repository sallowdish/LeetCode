class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m = []
        for col in range(len(matrix[0])):
            new_row = []
            for row in range(len(matrix) - 1, -1, -1):
                new_row.append(matrix[row][col])
            m.append(new_row)
        return m
