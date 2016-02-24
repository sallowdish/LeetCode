class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        max_sum = nums[0]
        sum_so_far = nums[0]
        for n in nums[1:]:
            new_sum = max(sum_so_far+n, n)
            if new_sum > max_sum:
                max_sum = new_sum
            sum_so_far = new_sum
        return max_sum
