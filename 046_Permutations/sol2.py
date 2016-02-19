class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        P = [[]]
        for n in nums:
            P_bar = []
            for p in P:
                for i in range(len(p) + 1):
                    P_bar.append(p[:i] + [n] + p[i:])
            P = P_bar
        return sorted(P)
