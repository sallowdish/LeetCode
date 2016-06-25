#!/usr/bin/python3
from unittest import TestCase, main
from sol1 import Solution
from collections import Counter


class Test(TestCase):
    board = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']]
    sol = None

    def setUp(self):
        self.sol = Solution()

    # test find_neighbors
    def test0_0(self):
        pos = (0, 0)
        ans = [(0, 1), (1, 0)]
        self.assertEqual(Counter(ans), Counter(self.sol.find_neighbors(pos, self.board)))

    def test0_1(self):
        pos = (2, 3)
        ans = [(1, 3), (2, 2)]
        self.assertEqual(Counter(ans), Counter(self.sol.find_neighbors(pos, self.board)))

    def test0_2(self):
        pos = (1, 2)
        ans = [(0, 2), (1, 1), (1, 3), (2, 2)]
        self.assertEqual(Counter(ans), Counter(self.sol.find_neighbors(pos, self.board)))

    # test search_character_in_board
    # initial cases
    def test1_0(self):
        character = "A"
        ans = [[(0, 0)], [(2, 0)]]
        self.assertEqual(sorted(ans), sorted(self.sol.search_character_in_board(self.board, character)))

    def test1_1(self):
        character = "E"
        ans = [[(0, 3)], [(2, 2)], [(2, 3)]]
        self.assertEqual(sorted(ans), sorted(self.sol.search_character_in_board(self.board, character)))

    # intermediate cases
    def test1_2(self):
        character = "E"
        ans = [[(1, 3), (0, 3)], [(1, 3), (2, 3)]]
        self.assertEqual(sorted(ans), sorted(self.sol.search_character_in_board(self.board, character, [[(1, 3)]])))

    def test1_3(self):
        character = "E"
        ans = [[(1, 3), (0, 3)], [(1, 3), (2, 3)], [(0, 2), (0, 3)]]
        self.assertEqual(sorted(ans), sorted(self.sol.search_character_in_board(
            self.board, character, [[(1, 3)], [(0, 2)]])))

    def test1_4(self):
        character = "E"
        ans = []
        self.assertEqual(Counter(ans), Counter(self.sol.search_character_in_board(self.board, character, [[(1, 1)]])))

    # whole test
    def test2_0(self):
        word = ""
        ans = True
        self.assertEqual(ans, self.sol.exist(self.board, word))

    def test2_1(self):
        word = "asffqefef"
        ans = False
        self.assertEqual(ans, self.sol.exist([[]], word))

    def test2_2(self):
        word = "asdfadfcwqefqewfewfefedfqwefqe"
        ans = False
        self.assertEqual(ans, self.sol.exist(self.board, word))

    def test2_3(self):
        word = "ABCCED"
        ans = True
        self.assertEqual(ans, self.sol.exist(self.board, word))

    def test2_4(self):
        word = "SEE"
        ans = True
        self.assertEqual(ans, self.sol.exist(self.board, word))

    def test2_5(self):
        word = "ABCB"
        ans = False
        self.assertEqual(ans, self.sol.exist(self.board, word))

    # time test
    def test3_0(self):
        board = ["aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                 "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                 "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                 "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                 "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                 "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                 "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                 "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                 "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                 "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaab"]
        word = (
            "baaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        ans = True
        self.assertEqual(ans, self.sol.exist(board, word))


if __name__ == "__main__":
    # logging.basicConfig( stream=sys.stderr )
    # logging.getLogger( "Test.testSomething" ).setLevel( logging.DEBUG )
    main()
