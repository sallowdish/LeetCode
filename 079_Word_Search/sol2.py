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
        path = []
        return self.rec_search_word_dfs(word, path, board)

    def rec_search_word_dfs(self, word, path, board):
        if not word:
            return True
        if not path:
            possible_next_pos = self.find_start_pos(board, word[0])
        else:
            last_pos = path[-1]
            possible_next_pos = self.find_neighbors(last_pos, board)
            possible_next_pos = [x for x in possible_next_pos if x not in path]
        for pos in possible_next_pos:
            if board[pos[0]][pos[1]] == word[0]:
                if self.rec_search_word_dfs(word[1:], path + [pos], board):
                    return True
        return False

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

    def find_start_pos(self, board, first_letter):
        ret = []
        row = range(len(board))
        col = range(len(board[0]))
        for i in row:
            for j in col:
                if board[i][j] == first_letter:
                    ret.append((i, j))
        return ret
