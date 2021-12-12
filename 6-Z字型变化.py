def convert(s, numRows):
    if len(s) == 1 or numRows == 1:
        return s
    strList = ["" for i in range(numRows)]
    result = ""
    row = 0   # numRows
    fex = -1
    for ch in s:
        if row == 0 or row == numRows-1:
            fex = -fex
        strList[row] += ch
        row += fex
    for str in strList:
        result += str
    return result

print(convert(s = "PAYPALISHIRING", numRows = 3))