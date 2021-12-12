class Solution:
    def candy(self, ratings: List[int]) -> int:
        childLen = len(ratings) 
        # initialize candyNum
        candyNum = [1] * len(ratings)
        # iterate forward
        for idxF in range(1, childLen):
            if ratings[idxF] > ratings[idxF-1]:
                candyNum[idxF] = candyNum[idxF-1] + 1
        # iterate backward 
        for idxB in range(childLen-2, -1, -1):
            if ratings[idxB] > ratings[idxB+1]:
                candyNum[idxB] = max(candyNum[idxB], candyNum[idxB+1]+1)
        return sum(candyNum)