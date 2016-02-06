# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root or not p or not q:
            return None
        if p.val > q.val:
            p, q = q, p
        trace_p = self.trace_node(root, p)
        trace_q = self.trace_node(root, q)
        for node in trace_q[::-1]:
            if node in trace_p:
                return node
        return None

    def trace_node(self, root, node):
        if not root:
            return []
        if root.val == node.val:
            return [root]
        elif root.val < node.val:
            ret = self.trace_node(root.right, node)
        else:
            ret = self.trace_node(root.left, node)
        if not ret:
            return ret
        else:
            return [root] + ret
