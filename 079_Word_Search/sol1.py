class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        # empty board or word is too long
        if not word:
            return True
        if not board or len(word) > len(board) * len(board[0]):
            return False
        start_position = []
        for c in word:
            start_position = self.search_character_in_board(board, c, start_position)
            if not start_position:
                return False
        return True

    def search_character_in_board(self, board, character, start_position=None):
        ret = []
        if not start_position:
            for row in range(len(board)):
                for col in range(len(board[0])):
                    cell = board[row][col]
                    if cell == character:
                        ret.append([(row, col), ])
        else:
            for path in start_position:
                last_pos = path[-1]
                neighbors = self.find_neighbors(last_pos, board)
                for neighbor in neighbors:
                    if neighbor not in path:
                        cell = board[neighbor[0]][neighbor[1]]
                        if cell == character:
                            ret.append(path + [neighbor])
        return ret

    def find_neighbors(self, pos, board):
        row = pos[0]
        col = pos[1]
        ret = []
        if row > 0:
            ret.append((row - 1, col))
        if row < len(board) - 1:
            ret.append((row + 1, col))
        if col > 0:
            ret.append((row, col - 1))
        if col < len(board[0]) - 1:
            ret.append((row, col + 1))
        return ret
