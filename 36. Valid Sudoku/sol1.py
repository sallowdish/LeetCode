class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for row in board:
            if not self.isPartitionValid(row):
                return False
        Tboard = [[board[row][col] for row in range(9)] for col in range(9)]
        for row in Tboard:
            if not self.isPartitionValid(row):
                return False
        for i in range(3):
            for j in range(3):
                l = []
                l.append(board[i * 3 ][j * 3 ])
                l.append(board[i * 3 +1][j * 3 ])
                l.append(board[i * 3 +2][j * 3 ])
                l.append(board[i * 3 ][j * 3 +1])
                l.append(board[i * 3 +1][j * 3 +1])
                l.append(board[i * 3 +2][j * 3 +1])
                l.append(board[i * 3 ][j * 3 +2])
                l.append(board[i * 3 +1][j * 3 +2])
                l.append(board[i * 3 +2][j * 3 +2])
                if not self.isPartitionValid(l):
                    return False
        return True


    def isPartitionValid(self,listStr):
        l = [i for i in listStr if i != "."]
        return len(l) == len(set(l))