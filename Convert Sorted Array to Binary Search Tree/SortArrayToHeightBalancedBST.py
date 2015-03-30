__author__ = 'rui.zheng'


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):

        def findMid(l):
            if len(l)==0:
                return None
            else:
                return l[int(len(l)/2)]

        def setnode(l, head, tail):
            if head > tail:
                return None
            elif head==tail:
                return TreeNode(l[head])
            else:
                newNode = TreeNode(findMid(l[head:tail]))
                newNode.left=setnode(l, head, int((head+tail)/2)-1)
                newNode.right=setnode(l, int((head+tail)/2)+1, tail)
                return newNode

        root = setnode(num, 0, len(num)-1)
        return root

    def traverse(self, rootnode):
        if rootnode is not None:
            thislevel = [rootnode]
            while thislevel:
                nextlevel = list()
                for n in thislevel:
                    print(n.val, end=" ")
                    if n.left:
                        nextlevel.append(n.left)
                    if n.right:
                        nextlevel.append(n.right)
                print()
                thislevel=nextlevel

lst = [0]
s = Solution()
ans = s.sortedArrayToBST(lst)
s.traverse(ans)
