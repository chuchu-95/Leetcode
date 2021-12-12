def isValid(s):
    dic = {"}": "{", ")": "(", "]": "["}
    arr = []
    index = -1
    for i in s:
        if i == "{" or i == "[" or i == "(":
            arr.append(i)
            index += 1
        elif i in dic:
            if arr != [] and dic[i] == arr[index]:
                arr.pop(index)
                index -= 1
            else:
                return False
    return True if arr == [] else False





