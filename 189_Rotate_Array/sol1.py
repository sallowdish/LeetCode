class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not len(nums):
            return nums
        k = k % len(nums)
        nums[:] = nums[k:] + nums[:k]
        return nums
