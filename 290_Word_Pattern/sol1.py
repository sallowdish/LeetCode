class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        keys = list(pattern)
        values = str.split()
        if len(keys) != len(values):
            return False
        mapping = {}
        for i in range(len(keys)):
            if keys[i] not in mapping:
                mapping[keys[i]] = values[i]
            else:
                if mapping[keys[i]] != values[i]:
                    return False
        return len(set(mapping.keys())) == len(set(mapping.values()))
