class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums or nums[0] > target:
            return 0
        elif nums[-1] < target:
            return len(nums)
        else:
            return self.binary_search(nums, target, 0, len(nums) - 1)

    def binary_search(self, nums, target, start, end):
        mid = int((start + end) / 2)
        if mid == start or mid == end:
            return start if nums[start] == target else end
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return self.binary_search(nums, target, mid, end)
        else:
            return self.binary_search(nums, target, start, mid)
