class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if len(nums) < 2:
            return [str(x) for x in nums]
        ranges = []
        start_value = curr_value = nums[0]
        isCont = 0
        for i in nums[1:]:
            if i - curr_value == 1:
                curr_value = i
                # print "%d continues" % i
            else:
                # print "%d breaks" % i
                if start_value != curr_value:
                    ranges.append("%s->%s" % (start_value, curr_value))
                else:
                    ranges.append(str(curr_value))
                start_value = curr_value = i
        # print "end with %d" % curr_value
        # print ranges, isCont
        if start_value != curr_value:
            ranges.append("%s->%s" % (start_value, curr_value))
        else:
            ranges.append(str(curr_value))

        return ranges
