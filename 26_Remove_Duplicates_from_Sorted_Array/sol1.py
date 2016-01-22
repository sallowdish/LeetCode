#!/usr/bin/python3
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        c = 1
        d = nums[0]
        for i in xrange(1, len(nums)):
            if d == nums[i]:
                continue
            else:
                nums[c] = nums[i]
                d = nums[i]
                c += 1
        return c