class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # dfs
        res = []
        self.helper(1, k, n, res, [])
        return res
    def helper(self, start, k, n, res, sub):
        if len(sub) == k:
            res.append(sub)
        else:
            for i in range(start, n+1):
                self.helper(i+1, k, n, res, sub+[i])