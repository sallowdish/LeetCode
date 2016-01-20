class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        index = 0
        while len(nums1) > m:
            nums1.pop()
        nums2 = nums2[:n]
        for i in nums2:
            try:
                d = nums1[index]
                while d < i:
                    index += 1
                    d = nums1[index]
                nums1.insert(index, i)
                index += 1
            except IndexError:
                nums1.append(i)
        return nums1




