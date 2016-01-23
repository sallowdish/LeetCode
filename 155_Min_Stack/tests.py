#!/usr/bin/python3
from unittest import TestCase, main
from sol1 import MinStack

class Test(TestCase):

    stack = None

    def setUp(self):
        self.stack = MinStack()

    # test __init__
    def test0(self):
        self.assertEqual(self.stack.dataSet, [])
        self.assertIsNone(self.stack.minIndex)

    # test __push__
    def test1(self):
        self.assertEqual(self.stack.push(1).dataSet, [1])
        self.assertEqual(self.stack.push(1).dataSet, [1,1])
        self.assertEqual(self.stack.push(2).dataSet, [1,1,2])

    # test __pop__
    def test2(self):
        self.stack.push(1).push(2).push(3)
        self.assertEqual(self.stack.pop(), 3)
        self.assertEqual(self.stack.dataSet, [1,2])
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.dataSet, [1])
        self.assertEqual(self.stack.pop(), 1)
        self.assertEqual(self.stack.dataSet, [])
        with self.assertRaises(IndexError):
            self.stack.pop()

    # test __top__
    def test3(self):
        self.stack.push(1).push(2).push(3)
        self.assertEqual(self.stack.top(), 3)
        self.assertEqual(self.stack.dataSet, [1,2,3])
        self.stack.pop()
        self.assertEqual(self.stack.top(), 2)
        self.assertEqual(self.stack.dataSet, [1,2])
        self.stack.pop()
        self.assertEqual(self.stack.top(), 1)
        self.assertEqual(self.stack.dataSet, [1])
        self.stack.pop()
        with self.assertRaises(IndexError):
            self.stack.top()

    # test __getMin__
    def test4(self):
        self.assertEqual(self.stack.getMin(), None)
        self.stack.push(1)
        self.assertEqual(self.stack.getMin(), 1)
        self.stack.push(-1)
        self.assertEqual(self.stack.getMin(), -1)
        self.stack.pop()
        self.assertEqual(self.stack.getMin(), 1)





if __name__ == "__main__":
    # logging.basicConfig( stream=sys.stderr )
    # logging.getLogger( "Test.testSomething" ).setLevel( logging.DEBUG )
    main()
