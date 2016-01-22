# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        ret =  self.recTraverse([x for x in (root.left,root.right) if x])
        ret.insert(0, [root.val])
        return ret

    def recTraverse(self, nodeList):
        if len(nodeList) == 0:
            return []
        valList = [x.val for x in nodeList]

        nextLayerNodeList = [node for x in nodeList for node in (x.left, x.right)]
        nextLayerNodeList = [x for x in nextLayerNodeList if x]
        ret = self.recTraverse(nextLayerNodeList)
        ret.insert(0, valList)
        return ret