import itertools


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = sorted(candidates)
        valid_candidate = [x for x in candidates if x < target]
        ret = []
        stack = []
        for i in range(len(valid_candidate)):
            stack.append(([valid_candidate[i]], i))
        while stack:
            combination = stack.pop(0)
            new_combination = []
            for i in range(combination[1] + 1, len(valid_candidate)):
                new_combination.append((combination[0] + [valid_candidate[i]], i))
            for nc in new_combination:
                if sum(nc[0]) == target:
                    ret.append(nc[0])
                elif sum(nc[0]) < target:
                    stack.append(nc)
                else:
                    continue
        if target in candidates:
            ret.append([target])
        ret.sort()
        return [ret for ret, _ in itertools.groupby(ret)]
