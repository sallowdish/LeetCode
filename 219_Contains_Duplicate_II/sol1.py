class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 2:
            return False
        if len(nums) == len(set(nums)):
            return False
        d = {}
        for i in range(len(nums)):
            integer = nums[i]
            if integer not in d:
                d[integer] = [i]
            else:
                d[integer].append(i)
        for value in d.values():
            if len(value) < 2:
                continue
            else:
                diffs = [value[i + 1] - value[i] for i in range(len(value) - 1)]
                for diff in diffs:
                    if diff <= k:
                        return True
        return False
