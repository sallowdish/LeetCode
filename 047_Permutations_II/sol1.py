class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        P = self.rec_permute([], nums)
        return P

    def rec_permute(self, root, candidates):
        if not candidates:
            return [root]
        P = []
        for i in range(len(candidates)):
            new_permutations = self.rec_permute(root + [candidates[i]], candidates[:i] + candidates[i + 1:])
            for p in new_permutations:
                if p not in P:
                    P.append(p)
        return P
