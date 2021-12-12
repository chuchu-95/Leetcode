class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # space Complexity: O(rowIndex)
        result = [0] * (rowIndex+1)
        for i in range(rowIndex+1):
            result[i] = 1
            for j in range(i-1, 0, -1):
                result[j] += result[j-1]
        return result

