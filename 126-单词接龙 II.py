class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        self.map = {}
        self.deepMap = {}
        self.result = []
        #bulidMap for str's next point str(just one word differ)
        self.bulidMap(beginWord, wordList)

        #bfs bulid layer
        self.minLen = self.bfs(beginWord, endWord)

        # dfs
        self.doneSet = set()
        currList = []
        currList.append(endWord)
        self.doneSet.add(endWord)
        self.dfs(currList, beginWord, 1)
        return self.result

    def bfs(self, beginWord, endWord):
        if beginWord == endWord:
            return 0
        #bfs
        queue = []
        queue.append(beginWord)
        self.deepMap[beginWord] = 0
        step = 1
        while queue: 
            size = len(queue)
            for i in range(size):
                wd = queue.pop(0)
                if wd == endWord:
                    return step
                if wd in self.map:
                    nxtStrList = self.map[wd]
                    for sub in nxtStrList:
                        #judge if it is 1-2, 2-1
                        if sub not in self.deepMap:
                            queue.append(sub)
                            self.deepMap[sub] = step
            step += 1
        return 0

    def dfs(self, currList, target, currDeep):
        currString = currList[0]
        if len(currList) > self.minLen:
            return
        elif len(currList) == self.minLen:
            if currString == target:
                self.result.append(currList[:])
        else:
            for sr in self.map[currString]:
                # sr isn't used and sr/currString not in same layer
                if sr not in self.doneSet and sr in self.deepMap and self.deepMap[sr] == self.deepMap[currString]-1:
                    currList.insert(0,sr)
                    self.doneSet.add(sr)
                    self.dfs(currList, target, currDeep+1)
                    self.doneSet.remove(sr)
                    currList.pop(0)

    def bulidMap(self, beginWord, wordList):
        wordSet = set()
        for s in wordList:
            wordSet.add(s)
        wordSet.add(beginWord)
        for st in wordSet:
            self.map[st] = []
            self.differ(st,wordSet)

    def differ(self, sg, wordSet):
        alph = list(map(chr, range(ord('a'), ord('z') + 1)))
        for i in range(len(sg)):
            sb = list(sg)
            curr = sb[i]
            for ch in alph:
                if curr != ch:
                    sb[i] = ch
                    sbStr = "".join(sb)
                    if sbStr in wordSet:
                        self.map[sg].append(sbStr)