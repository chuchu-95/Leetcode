class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return 
        if m == 0:
            nums1[0] = nums2[0]
        point1 = m - 1
        point2 = n - 1
        reve = m + n - 1 
        while point1 >= 0 or point2 >= 0:
            if point1 == -1:
                nums1[reve] = nums2[point2]
                point2 -= 1
            elif point2 == -1:
                nums1[reve] = nums1[point1]
                point1 -= 1
            elif nums1[point1] > nums2[point2]:
                nums1[reve] = nums1[point1]
                point1 -= 1
            else:
                nums1[reve] = nums2[point2]
                point2 -= 1
            reve -= 1

        
            