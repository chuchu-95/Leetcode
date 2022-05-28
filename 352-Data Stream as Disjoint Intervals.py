class SummaryRanges:

    def __init__(self):
        self.interval = []

    def addNum(self, val: int) -> None:
        length = len(self.interval)
        if length == 0:
            self.interval.append([val, val])
            return 
        left = 0
        right = length - 1
        while left < right:
            mid = left + (right - left + 1) // 2
            if self.interval[mid][0] <= val:
                left = mid
            else:
                right = mid - 1
        curLst = self.interval[right]
        # interval has only one element or add interval at firat position
        if curLst[0] > val:
            if val + 1 == curLst[0]:
                self.interval[right][0] = val
            else:
                self.interval.insert(0, [val, val])
            return
        if val >= curLst[0] and val <= curLst[1]:
            return
        # normal situation: curLst[1] <= val
        if right == length - 1:
            if val - 1 == curLst[1]:
                self.interval[right][1] = val
            else:
                self.interval.append([val, val])
        else:
            nxtLst = self.interval[right+1]
            # merge two intervals
            if val-1 == curLst[1] and val+1 == nxtLst[0]:
                self.interval[right][1] = nxtLst[1]
                self.interval.pop(right+1)
            elif val-1 == curLst[1]:
                self.interval[right][1] = val
            elif val+1 == nxtLst[0]:
                self.interval[right+1][0] = val
            else:
                self.interval.insert(right+1, [val, val])

    def getIntervals(self) -> List[List[int]]:
        return self.interval



# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()


#java
# class SummaryRanges {
#     TreeMap<Integer, Integer> tree;
#     public SummaryRanges() {
#         // key is the start of interval
#         tree = new TreeMap<>();
#     }
    
#     public void addNum(int val) {
#         if(tree.containsKey(val)){
#             return;
#         }
#         Integer low = tree.lowerKey(val);
#         Integer high = tree.higherKey(val);
#         //merge two
#         if(low != null && high != null && tree.get(low)+1 == val && high-1 == val){
#             tree.put(low, tree.get(high));
#             //tree.get(low) = tree.get(high);
#             tree.remove(high);
#         }
#         //merge one interval or val in cur interval and do nothing
#         //prev interval
#         else if(low != null && tree.get(low)+1 >= val){
#             //tree.get(low) = Math.max(tree.get(low), val); 
#             tree.put(low, Math.max(tree.get(low), val));
#         }
#         //next interval
#         else if(high != null && high-1 == val){ 
#             tree.put(val, tree.get(high));
#             tree.remove(high);
#         }
#         //create new interval
#         else{
#             tree.put(val, val);
#         }
#     }
    
#     public int[][] getIntervals() {
#         //return new ArrayList<>(tree.values());
#         List<int[]> res = new ArrayList<>();
#         for(int key : tree.keySet()){
#             res.add(new int[]{key, tree.get(key)});
#         }
#         return res.toArray(new int[tree.size()][2]);
#     }
# }

# /**
#  * Your SummaryRanges object will be instantiated and called as such:
#  * SummaryRanges obj = new SummaryRanges();
#  * obj.addNum(val);
#  * int[][] param_2 = obj.getIntervals();
#  */