class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        answer = [-1] * len(queries)
        start = 10 ** ((intLength-1)//2)
        end = 10 ** ((intLength-1)//2+1) - 1

        for idx, query in enumerate(queries):
            curNum = start + query - 1
            curStr = str(curNum)
            if intLength % 2 != 0:
                num = curStr + curStr[-2::-1]     
            else:
                num = curStr + curStr[-1::-1]        
            if len(num) > intLength:
                continue
            answer[idx] = int(num)
        return answer