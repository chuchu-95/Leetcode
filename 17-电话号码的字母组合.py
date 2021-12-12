def help(per, index, digits, dictionary, result):
    if index == len(digits):
        result.append(per)
    else:
        num = digits[index]
        if num in dictionary:
            for ch in dictionary[num]:
                help(per+ch, index+1, digits, dictionary, result)

        
def letterCombinations(digits):
    phone_dict = {"2":["a","b","c"], "3":["d","e","f"], "4":["g","h","i"], "5":["j","k","l"], 
            "6":["m","n","o"], "7":["p","q","r","s"], "8":["t","u","w"], "9":["w","x","y","z"]}
    result = []
    help("", 0, digits, phone_dict, result)
    return result

print(letterCombinations("234"))