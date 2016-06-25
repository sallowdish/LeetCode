from unittest import TestCase, main
from Solution import Solution


class Test(TestCase):
    sol = None
    data = None

    def setUp(self):
        self.sol = Solution()
        self.data = (
            (("a", ["a"]), True),
            (("a", ["b"]), False),
            (("Leetcode", ["Leet", "code"]), True),
            (("goalspecial", ["go", "goal", "goals", "special"]), True)
        )

    def test_sol(self):
        for input_data, result in self.data:
            s, word_dict = input_data[0], input_data[1]
            self.assertEqual(result, self.sol.wordBreak(s, word_dict), input_data)

if __name__ == '__main__':
    main()
