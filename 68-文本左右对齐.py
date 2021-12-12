class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        start = 0
        end = 0
        while end < len(words):
            cnt = 0
            lenLst = []
            while end < len(words) and cnt <= maxWidth:
                lenWord = len(words[end])
                lenLst.append(lenWord)
                cnt += lenWord
                cnt += 1 # fix space
                end += 1

            if cnt <= maxWidth+1:
                end -= 1
            if cnt > maxWidth+1:
                lenLst.pop()
                end -= 2
            sub = ""
            sub += words[start]
            rest = maxWidth - lenLst[0]
            # just have one word
            if start == end:
                st = " " * rest
                sub += st
            # last line
            elif end == len(words)-1:
                for j in range(start+1, end+1):
                    st = " " + words[j]
                    sub += st
                if len(sub) < maxWidth:
                    sub += (" "*(maxWidth-len(sub)))
            else:
                space = rest - sum(lenLst[1::])
                judge = space % (len(lenLst)-1)
                divid = space // (len(lenLst)-1)
                for i in range(start+1, end+1):
                    if judge > 0:
                        st = " "*(divid+1) + words[i]
                    else:
                        st = " "*divid + words[i]
                    sub += st      
                    judge -= 1
            result.append(sub)
            start = end + 1
            end += 1
        return result
              
            



