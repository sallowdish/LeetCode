import pdb


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        if not wordDict:
            return False
        # pdb.set_trace()
        return self.rec_split_string("", s, wordDict)

    def rec_split_string(self, pattern, s, wordDict):
        if not pattern:
            print "start over with %s" % s
        if not s:
            return False
        count = 1
        while count <= len(s):
            first_section = pattern + s[:count]
            if first_section in wordDict:
                # nothing left or the rest is a word in dict as well
                if not s[count:] or s[count:] in wordDict:
                    return True
                else:
                    if self.rec_split_string("", s[count:], wordDict):
                        return True

            count += 1
        return False
