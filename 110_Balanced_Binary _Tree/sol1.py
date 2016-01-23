# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    isBalance = True
    
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.recFindDepth(root)
        return self.isBalance
        
    def recFindDepth(self,root):
        if not root or not self.isBalance:
            return 0
        left=self.recFindDepth(root.left)
        right=self.recFindDepth(root.right)
        if abs(left-right) > 1:
            self.isBalance = False
        return max(left, right) + 1