class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        P = self.rec_permute([], nums)
        return sorted([list(x) for x in P])

    def rec_permute(self, root, candidates):
        if not candidates:
            return {tuple(root)}
        P = set()
        for i in range(len(candidates)):
            new_permutations = self.rec_permute(root + [candidates[i]], candidates[:i] + candidates[i + 1:])
            P = P.union(new_permutations)
        return P
