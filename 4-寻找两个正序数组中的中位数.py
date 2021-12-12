def findMedianSortedArrays(nums1, nums2):
    #planA (m+n)log(m+n)
    # nums = nums1 + nums2
    # def quickSort(arr):
    #     if len(arr) < 2:
    #         return arr
    #     else:
    #         pivot = arr[0]
    #         less = [i for i in arr[1:] if i <= pivot]
    #         big = [i for i in arr[1:] if i > pivot]
    #         return quickSort(less) + [pivot] + quickSort(big)
    # nums_sort = quickSort(nums)
    # print(n+ums_sort)
    # long = len(nums_sort)
    # return nums_sort[long//2] if long%2 != 0 else (nums_sort[long//2] + nums_sort[long//2+1])/2


    # m+n
    # ans = []
    # pointA = 0
    # pointB = 0
    # while True:
    #     if pointA == len(nums1):
    #         ans += nums2[pointB: ]
    #         break
    #     if pointB == len(nums2):
    #         ans += nums1[pointA: ]
    #         break

    #     if nums1[pointA] <= nums2[pointB]:
    #         ans.append(nums1[pointA])
    #         pointA += 1  
    #     else:
    #         ans.append(nums2[pointB])
    #         pointB += 1
    #           
    # long = len(ans)
    # print(ans)
    # return ans[long//2] if long%2 != 0 else (ans[long//2] + ans[long//2-1])/2

    # min(m, n)
    # li1, li2 = (nums1, nums2) if len(nums1) < len(nums2) else (nums2, nums1)
    # long1 = len(li1)
    # long2 = len(li2)
    # if not li1:
    #     return (li2[long2 // 2]+li2[long2 // 2 - 1])/2 if long2 % 2 == 0 else li2[long2 // 2]
    # sp = (long1+long2+1) // 2
    # i = 0
    # while i <= long1:
    #     j = sp - i
        
    #     li1_left = li2[j-1] if i == 0 else li1[i-1]
    #     li1_right = li2[j] if i == long1 else li1[i]
    #     li2_left = li1[i-1] if j == 0 else li2[j-1]
    #     li2_right = li1[i] if j == long2 else li2[j]
    #     if li1_left <= li2_right:
    #         left_max = max(li1_left, li2_left)
    #         right_min = min(li1_right, li2_right)
    #     i += 1
    # return (left_max+right_min)/2 if (long1+long2)%2 == 0 else left_max
    
    # log min(m, n)
    li1, li2 = (nums1, nums2) if len(nums1) < len(nums2) else (nums2, nums1)
    long1 = len(li1)
    long2 = len(li2)  
    if not li1:
        return (li2[long2 // 2]+li2[long2 // 2 - 1])/2 if long2 % 2 == 0 else li2[long2 // 2] 
    sp = (long1+long2+1) // 2
    i = (long1 + 1) // 2 
    j = sp - i
    low, high = 0, long1
    while low < high:  
        if i < long1 and li2[j-1] > li1[i]:
            low = i + 1
        else:
            high = i
        
        i = (low + high)//2
        j = sp - i

    li1_left = li2[j-1] if i == 0 else li1[i-1]
    li1_right = li2[j] if i == long1 else li1[i]
    li2_left = li1[i-1] if j == 0 else li2[j-1]
    li2_right = li1[i] if j == long2 else li2[j] 
    left_max = max(li1_left, li2_left)
    right_min = min(li1_right, li2_right)
    
    return (left_max+right_min)/2 if (long1+long2)%2 == 0 else left_max


print(findMedianSortedArrays([1,3], [2]))

