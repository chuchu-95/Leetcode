class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        self.dfsHelper2(0, len(candidates), candidates, target, result, [])
        return result
    def dfsHelper2(self, start, end, candidates, target, result, contain):
        if target == 0:
            result.append(contain)
        # the candidates have same nums, so first sort it 
        elif target > 0:
            for i in range(start, end):
                #the candidate have already been sorted
                if candidates[i] > target:
                    break
                if i > start and candidates[i-1] == candidates[i]:
                    continue
                self.dfsHelper2(i+1, end, candidates, target-candidates[i], result, contain+[candidates[i]])