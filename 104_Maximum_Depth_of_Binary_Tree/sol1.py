 # Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return self.recFindMaxDepty([node for node in (root.left, root.right) if node]) +1

    def recFindMaxDepty(self, nodeList):
        if len(nodeList) == 0:
            return 0
        nextLayerNodeList = [node for x in nodeList for node in (x.left, x.right) if node]
        return self.recFindMaxDepty(nextLayerNodeList) + 1
