# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.recPreOrderTraverse([root.left],[root.right])

    def recPreOrderTraverse(self, nodeListLeft, nodeListRight):
        if len(nodeListLeft) == len(nodeListRight) == 0:
            return True
        if len(nodeListLeft) != len(nodeListRight):
            return False
        valueListLeft = [x.val if x else x for x in nodeListLeft]
        valueListRight = [x.val if x else x for x in nodeListRight]
        if valueListLeft != valueListRight[::-1]:
            return False
        nodeListLeft = [x for x in nodeListLeft if x ]
        nodeListRight = [x for x in nodeListRight if x]
        nextLayerNodeListLeft = [node for x in nodeListLeft for node in (x.left, x.right)]
        nextLayerNodeListRight = [node for x in nodeListRight for node in (x.left, x.right)]
        return self.recPreOrderTraverse(nextLayerNodeListLeft, nextLayerNodeListRight)