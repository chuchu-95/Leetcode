class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        array = [[0 for i in range(len(obstacleGrid[0]))] for j in range(len(obstacleGrid))]
        # initalize
        for ob1 in range(len(obstacleGrid[0])):
            if obstacleGrid[0][ob1] == 1:
                break
            else:
                array[0][ob1] = 1
        for ob2 in range(len(obstacleGrid)):
            if obstacleGrid[ob2][0] == 1:
                break
            else:
                array[ob2][0] = 1
        # start
        for m in range(1, len(obstacleGrid)):
            for n in range(1, len(obstacleGrid[0])):
                if obstacleGrid[m][n] == 1:
                    array[m][n] = 0
                else:
                    array[m][n] = array[m-1][n] + array[m][n-1]
        return array[len(obstacleGrid)-1][len(obstacleGrid[0])-1]