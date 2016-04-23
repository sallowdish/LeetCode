from collections import Counter


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        prev = []
        ret = []
        if not nums:
            return [[]]
        count = Counter(nums)
        element_set = sorted(count.keys())
        for i in range(len(nums)):
            if i == 0:
                prev = [[]]
                ret += prev
            else:
                temp = []
                for p in prev:
                    if not p:
                        temp = [[x] for x in element_set]
                        break
                    last_element = p[-1]
                    next_element = [x for x in element_set if x > last_element]
                    if p.count(last_element) != count[last_element]:
                        # there is more identical element
                        next_element.insert(0, last_element)
                    for n in next_element:
                        new_subset = p + [n]
                        temp.append(new_subset)
                prev = temp
                ret += temp
        return ret + [sorted(nums)]

    @staticmethod
    def find_next_element(x, lst):
        for i in lst:
            if i <= x:
                continue
            return i
