class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        self.dfsHelper(0, len(candidates), candidates, target, result, [])
        return result
    def dfsHelper(self, start, end, candidates, target, result, contain):
        if target == 0:
            result.append(contain)
        elif target > 0:
            for i in range(start, end):
                if candidates[i] <= target:
                    self.dfsHelper(i, end, candidates, target-candidates[i], result, contain+[candidates[i]])
# same as leetcode17, dfs
# when use dfsHelper, don't change target, just transfer into function