class Solution:
    def canCompleteCircuit(self, gas,cost) :
        # currGas - cost[i] + gas[i+1]
        nLen = len(gas)
        # find min rest gas, idx+1 is the start point
        # if gas[i] < cost[i], this point is definitely not the start point
        minRest = None
        totalRest = 0
        idx = 0
        minIdx = 0
        while idx < nLen:
            totalRest += (gas[idx] - cost[idx])
            if minRest == None:
                minRest = totalRest
            elif totalRest <= minRest:
                minRest = totalRest
                minIdx = idx
            idx += 1
        return -1 if totalRest < 0 else (minIdx+1) % nLen
        
