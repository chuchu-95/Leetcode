def intToRoman(num):
    roman = ""
    while num != 0:
        divi = 10 ** (len(str(num))-1)
        a = num // divi
        roman += change(divi, a)
        num = num % divi
    return roman
        
def change(divi, a):
    result = ""
    dict_roman = {1: "I", 10: "X", 100: "C", 1000: "M"} 
    list_roman = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    index__a = list_roman.index(dict_roman[divi])
    if a in range(1, 4):
        result += a*dict_roman[divi]
    elif a == 4:
        result += list_roman[index__a] + list_roman[index__a+1]
    elif a == 5:
        result += list_roman[index__a+1]
    elif a in range(6, 9):
        m = a - 5
        result += list_roman[index__a+1] + change(divi, m)
    elif a == 9:
        result += list_roman[index__a] + list_roman[index__a+2]
    return result
    
print(intToRoman(1994))
# print(change(100, 4))