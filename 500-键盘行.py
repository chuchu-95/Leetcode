def findWords(words):
    a = []
    set1_num = set("qwertyuiop")
    set2_num = set("asdfghjkl")
    set3_num = set("zxcvbnm")
    for i in words:
        i_re = set(i.lower())
        if i_re <= set1_num or i_re <= set2_num or i_re <= set3_num:
            a.append(i)
    return a

print(findWords(["Hello", "Alaska", "Dad", "Peace"]))
