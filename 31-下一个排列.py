class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums)-2
        while i > 0:
            if nums[i] < nums[i+1]:
                break
            i -= 1
        j = len(nums)-1
        while j > i:
            if nums[j] > nums[i]:
                break
            j -= 1
        self.exchange(i, j, nums)
        self.sort_part(i, j, nums)

        
    def exchange(self, i, j, nums):
        b = nums[j]
        nums[j] = nums[i]
        nums[i] = b 
        return nums
    def sort_part(self, i, j, nums):
        if i == 0 and j == 0:
            head = i
        else:
            head = i+1
        tail = len(nums)-1
        cnt = (tail-head+1) // 2
        while cnt > 0:
            self.exchange(head, tail, nums)
            head += 1
            tail -= 1
            cnt -= 1