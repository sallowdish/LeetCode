class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        return self.rec_permute([], nums)

    def rec_permute(self, root, candidates):
        if not candidates:
            return [root]
        P = []
        for i in candidates:
            P += self.rec_permute(root+[i], [x for x in candidates if i != x])
        return P
