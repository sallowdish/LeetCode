class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        current_min = 0
        for i in range(len(nums)):
            is_swap = False
            while current_min < 3:
                if nums[i] == current_min:
                    break
                for j in range(i + 1, len(nums)):
                    if nums[j] == current_min:
                        nums[i], nums[j] = nums[j], nums[i]
                        is_swap = True
                        break
                if is_swap:
                    break
                else:
                    current_min += 1
        return nums
