class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]
        nums = sorted(nums)
        ret = [[]]
        shorter_subsets = []
        for l in range(len(nums)):
            # length of current subset
            l += 1
            if l == 1:
                subsets = []
                for index in range(len(nums)):
                    subsets.append(([nums[index]], index))
            else:
                subsets = []
                for subset_entry in shorter_subsets:
                    s = subset_entry[0]
                    start_index = subset_entry[1] + 1
                    for index in range(start_index, len(nums)):
                        new_subset = s + [nums[index]]
                        new_subset_entry = (new_subset, index)
                        subsets.append(new_subset_entry)
            ret += [x[0] for x in subsets]
            shorter_subsets = subsets
        return ret
