#!/usr/bin/env python3
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in nums:
            diff = target - i
            if diff != i and diff in nums:
                (a, b) = (nums.index(i), nums.index(diff))
                if a<b :
                    return [a,b]
                else: 
                    return [b,a]