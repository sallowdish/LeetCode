class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m = [[row[i] for row in matrix[::-1]] for i in range(len(matrix[0]))]
        return m
