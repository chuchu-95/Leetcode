class Solution:
    def generateParenthesis(self, n: int) -> List[str]: 
        res = []
        self.generate(n, "", 0, 0, res)
        return res
    def generate(self, n, current, left, right, res):
        if left == n and right == n:
            res.append(current)

        if left < n:
            self.generate(n, current+"(", left+1, right, res)
        if right < left:
            self.generate(n, current+")", left, right+1, res)
