class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) == nums.count(0):
            return nums
        length = len(nums)
        index = count = 0
        while index < length:
            if nums[index - count] == 0:
                del nums[index - count]
                nums.append(0)
                count += 1
            index += 1
        return nums
