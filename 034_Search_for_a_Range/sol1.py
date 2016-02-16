class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums or nums[0] > target or nums[-1] < target:
            return [-1, -1]
        if nums[0] == target:
            mid = 0
        elif nums[-1] == target:
            mid = len(nums) - 1
        else:
            mid = self.binary_search(nums, target, 0, len(nums) - 1)
        if mid == -1:
            return [-1, -1]
        return self.expand(nums, target, mid)

    def binary_search(self, nums, target, start, end):
        if start >= end:
            # not found
            return -1
        mid = int((start + end) / 2)
        if mid == start or mid == end:
            return -1
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return self.binary_search(nums, target, mid, end)
        else:
            return self.binary_search(nums, target, start, mid)

    def expand(self, nums, target, mid):
        prev = mid - 1
        while prev >= 0:
            if nums[prev] == target:
                prev -= 1
            else:
                prev += 1
                break
        next = mid + 1
        while next < len(nums):
            if nums[next] == target:
                next += 1
            else:
                next -= 1
                break
        return [prev if prev > 0 else 0, next if next < len(nums) else len(nums) - 1]
