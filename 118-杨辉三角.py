class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        #initialize
        result.append([1])
        result.append([1,1])
        if numRows == 1:
            return [result[0]]
        if numRows == 2:
            return result
        row = 3
        while row <= numRows:
            sub = []
            sub.append(1)
            for i in range(len(result[row-2])-1):
                sub.append(result[row-2][i]+result[row-2][i+1])
            sub.append(1)
            result.append(sub)
            row += 1
        return result