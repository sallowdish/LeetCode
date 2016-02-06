#!/usr/bin/python3
from unittest import TestCase, main
from sol1 import Solution


class Test(TestCase):
    sol = None

    def setUp(self):
        self.sol = Solution()

    def test0(self):
        pattern = "abba"
        str = "dog cat cat dog"
        ans = True
        self.assertEqual(ans, self.sol.wordPattern(pattern, str))

    def test1(self):
        pattern = "abba"
        str = "dog cat cat fish"
        ans = False
        self.assertEqual(ans, self.sol.wordPattern(pattern, str))

    def test2(self):
        pattern = "abba"
        str = "dog dog dog dog"
        ans = False
        self.assertEqual(ans, self.sol.wordPattern(pattern, str))

    def test3(self):
        pattern = "abba"
        str = "dog dog dog dog"
        ans = False
        self.assertEqual(ans, self.sol.wordPattern(pattern, str))

    def test4(self):
        pattern = "abbc"
        str = "a b b aadwefweaedfcaewfcaewfqewfwef"
        ans = True
        self.assertEqual(ans, self.sol.wordPattern(pattern, str))


if __name__ == "__main__":
    # logging.basicConfig( stream=sys.stderr )
    # logging.getLogger( "Test.testSomething" ).setLevel( logging.DEBUG )
    main()
