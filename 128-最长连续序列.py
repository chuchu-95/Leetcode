class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longSerial = 0
        if nums == []:
            return longSerial
        numSet = set()
        for n in nums:
            numSet.add(n)
        # numSet     
        for num in numSet:
            preLong = longSerial
            if num-1 not in numSet:
                longSerial = 1
                currNum = num + 1
                while currNum in numSet:
                    longSerial += 1
                    currNum += 1
                longSerial = max(longSerial, preLong)
        return longSerial 
