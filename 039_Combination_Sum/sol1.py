class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = sorted(candidates)
        ret = []
        stack = [[x] for x in candidates if x < target]
        while stack:
            combination = stack.pop(0)
            new_combination = []
            for i in range(candidates.index(combination[-1]), len(candidates)):
                new_combination.append(combination + [candidates[i]])
            for nc in new_combination:
                if sum(nc) == target:
                    ret.append(nc)
                elif sum(nc) < target:
                    stack.append(nc)
                else:
                    continue
        if target in candidates:
            ret.append([target])
        return sorted(ret)
