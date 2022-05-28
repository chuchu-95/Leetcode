class Solution:
    def compress(self, chars: List[str]) -> int:
        point = 0 
        slow = 0
        fast = 0
        while fast < len(chars):
            while fast < len(chars) and chars[fast] == chars[slow]:
                fast += 1
            temp = chars[slow]
            chars[point] = temp
            point += 1
            if fast != slow + 1:
                cnt = fast - slow
                for s in str(cnt):
                    chars[point] = s
                    point += 1
            slow = fast
        return point
                