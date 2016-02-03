class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 1
        return len(nums) != len(d)
