class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        next_row = 1
        while next_row < len(matrix):
            boundary = matrix[next_row][0]
            if target == boundary:
                return True
            if target < boundary:
                # search previous row
                for i in matrix[next_row - 1]:
                    if i == target:
                        return True
                return False
            next_row += 1
        for i in matrix[-1]:
            if i == target:
                return True
        return False
