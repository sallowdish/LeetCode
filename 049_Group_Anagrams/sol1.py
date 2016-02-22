class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        for word in strs:
            k = "".join(sorted(word))
            if k in d:
                d[k] += [word]
            else:
                d[k] = [word]
        # return sorted([sorted(d[x]) for x in d], key=lambda x:-len(x))
        return [sorted(d[x]) for x in d]
