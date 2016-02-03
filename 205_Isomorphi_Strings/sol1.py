class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ###
        # build dict for (key = char, value = [occurrence])
        # compare dict to check if s and t are isomorphic
        ###
        dict1 = self.strToDict(s)
        dict2 = self.strToDict(t)

        return sorted(dict1.values()) == sorted(dict2.values())

    def strToDict(self, s):
        if not len(s):
            return {}
        ret = {}
        for i in range(len(s)):
            char = s[i]
            if char in ret:
                ret[char].append(i)
            else:
                ret[char] = [i]
        return ret