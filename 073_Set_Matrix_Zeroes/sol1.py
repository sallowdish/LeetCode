class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # to_be_zore_row = set()
        to_be_zore_col = set()
        to_be_zore_row = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    to_be_zore_row.add(i)
                    to_be_zore_col.add(j)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in to_be_zore_row or j in to_be_zore_col:
                    matrix[i][j] = 0
        return matrix
