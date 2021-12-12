class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        result = []
        word_dict = {}
        for word in words:
            if word in word_dict:
                word_dict[word] += 1
            else:
                word_dict[word] = 1
        s_len = len(s)
        w_len = len(words)
        word_len = len(words[0])
        for i in range(s_len - w_len*word_len + 1):
            dump = word_dict.copy()
            cnt = 0
            j = i
            while cnt < w_len:
                s_substring = s[j: j+word_len]
                if s_substring not in dump or dump[s_substring] == 0:
                    break
                dump[s_substring] -= 1
                j += word_len
                cnt += 1
            if cnt == w_len:
                result.append(i)
        return result