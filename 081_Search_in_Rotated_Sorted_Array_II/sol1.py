class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if target == nums[0]:
            return 0
        for i in range(1, len(nums)):
            if nums[i] == target:
                return i
            if nums[i] < nums[i - 1]:
                if target < nums[i] or target > nums[0]:
                    return -1
                left_nums = nums[i:]
                left_index = self.binary_search(left_nums, target)
                return -1 if left_index == -1 else left_index + i
        return -1

    def binary_search(self, nums, target):
        if target < nums[0] or target > nums[-1]:
            return -1
        if nums[0] == target:
            return 0
        if nums[-1] == target:
            return len(nums) - 1
        return self.rec_binary_search(nums, 0, len(nums) - 1, target)

    def rec_binary_search(self, nums, start, end, target):
        if start + 1 == end:
            return -1
        mid = (start + end) // 2
        if target == nums[mid]:
            return mid
        elif nums[mid] < target:
            return self.rec_binary_search(nums, mid, end, target)
        else:
            return self.rec_binary_search(nums, start, mid, target)
