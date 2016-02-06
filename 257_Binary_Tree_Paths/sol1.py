# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        if not root.left and not root.right:
            return ["%d" % root.val]
        return self.rec_path_root_to_leaf(root.left, str(root.val)) + self.rec_path_root_to_leaf(root.right,
                                                                                                 str(root.val))

    def rec_path_root_to_leaf(self, node, pattern):
        if not node:
            return []
        if not node.left and not node.right:
            return [pattern + "->%d" % node.val]
        else:
            pattern += "->%d" % node.val
            return self.rec_path_root_to_leaf(node.left, pattern) + self.rec_path_root_to_leaf(node.right, pattern)
