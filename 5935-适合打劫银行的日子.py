class Solution:
    def goodDaysToRobBank(self, security, time: int):
        if time == 0:
            return [i for i in range(len(security))]
        # time >= 1
        res = []
        if len(security) < 3:
            return res
        
        idxLst = []
        for i in range(1, len(security)-1):
            if security[i] <= security[i-1] and security[i] <= security[i+1]:
                idxLst.append(i)
        if time == 1:
            return idxLst
        for idx in idxLst:
            cnt = time
            left = idx - time
            right = idx + time
            if left < 0 or right > len(security)-1:
                continue
            else:
                while cnt > 0:
                    if security[left] >= security[left+1] and security[right] >= security[right-1]:
                        left += 1
                        right -= 1
                        cnt -= 1
                    else:
                        break
                if cnt == 0:
                    res.append(idx)
        return res
            
            