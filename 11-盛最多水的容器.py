# def maxArea(height):
    # O(n^2)
    # maxWater = 0
    # for i in range(len(height)):
    #     for j in range(1, len(height)):
    #         area = (j-i) * min(height[i], height[j])
    #         if area > maxWater:
    #             maxWater = area
    # return maxWater

def maxArea(height):
    maxWater = 0
    point1 = 0
    point2 = len(height) - 1
    while point1 != point2:
        area = (point2-point1) * min(height[point1], height[point2])
        if area >= maxWater:
            maxWater = area

        if height[point1] < height[point2]:
            point1 += 1
        else:
            point2 -= 1
    return maxWater

print(maxArea([1,8,6,2,5,4,8,3,7]))