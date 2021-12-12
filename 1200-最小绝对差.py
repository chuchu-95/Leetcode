#先排序，找出挨得最近的两个元素（一定是相邻的），找出最近的距离。
# 遍历数组，如果相邻元素的距离是最近距离，那么将这两个元素放入数组中。
def minimumAbsDifference(arr):
    arr.sort()
    li = []
    lis = []
    for i in range(1, len(arr)):
        li.append(arr[i]-arr[i-1])
    for j in range(len(arr)-1):
        if li[j] == min(li):
            lis.append([arr[j], arr[j+1]])
    return lis

def minimumAbsDifference(arr):
        arr.sort()
        lis = []
        limin = arr[1]-arr[0]
        for i in range(1, len(arr)):
            litmp = arr[i]-arr[i-1]
            if litmp < limin:
                lis = []
                lis.append([arr[i-1],arr[i]])
                limin = litmp
            elif (litmp==limin):
                lis.append([arr[i-1],arr[i]])
            else:
                continue
        return lis

print(minimumAbsDifference([3,8,-10,23,19,-4,-14,27]))







