# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        return self.recPreOrderTraverse(p,q)

    def recPreOrderTraverse(self, p, q):
        if p is None and q is None:
            return True
        elif p and q:
            # check value
            if p.val != q.val:
                return False
            #check structure
            else:
                return self.recPreOrderTraverse(p.left,q.left) and self.recPreOrderTraverse(p.right, q.right)
        else:
            return False