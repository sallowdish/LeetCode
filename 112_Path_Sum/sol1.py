# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        l = self.recLeafToRootSum(root)
        return sum in l

    def recLeafToRootSum(self, node):
        if not node:
            return []
        if not node.left and not node.right:
            return [node.val]
        else:
            sumFromBelow = self.recLeafToRootSum(node.left) + self.recLeafToRootSum(node.right)
            return [x + node.val for x in sumFromBelow]