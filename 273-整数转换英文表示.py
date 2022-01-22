class Solution:
    def numberToWords(self, num: int) -> str:
        res = ""
        if num == 0:
            return "Zero"
        n = num
        # back to forward
        part1 = n % 1000
        n //= 1000

        part2 = n % 1000
        n //= 1000

        part3 = n % 1000
        n //= 1000

        part4 = n
        if part4 != 0:
            res += self.outPut(part4) + "Billion "
        if part3 != 0:
            res += self.outPut(part3) + "Million "
        if part2 != 0:
            res += self.outPut(part2) + "Thousand "
        res += self.outPut(part1)
        return res.strip(" ")
    
    # num < 1000
    def outPut(self, num):
        sub = ""
        a = num // 100
        sub += self.oneDigit(a)
        if a != 0:
            sub += "Hundred "
        num %= 100
        if num >= 20:
            b = num - (num % 10)
            sub += self.tyNum(b)
            num %= 10
        elif num >= 10 and num < 20:
            sub += self.twoDigit(num)
            num = 0       
        sub += self.oneDigit(num)
        return sub

    def oneDigit(self, num):
        oneDict = {
            1 : "One ",
            2 : "Two ",
            3 : "Three ",
            4 : "Four ",
            5 : "Five ",
            6 : "Six ",
            7 : "Seven ",
            8 : "Eight ",
            9 : "Nine ",
        }
        return oneDict.get(num, "") 
    def twoDigit(self, num):
        twoDict = {
            10 : "Ten ",
            11 : "Eleven ",
            12 : "Twelve ",
            13 : "Thirteen ",
            14 : "Fourteen ",
            15 : "Fifteen ",
            16 : "Sixteen ",
            17 : "Seventeen ",
            18 : "Eighteen ",
            19 : "Nineteen "
        }
        return twoDict.get(num, "") 
    def tyNum(self, num):
        tyDict = {
            20 : "Twenty ",
            30 : "Thirty ",
            40 : "Forty ",
            50 : "Fifty ",
            60 : "Sixty ",
            70 : "Seventy ",
            80 : "Eighty ",
            90 : "Ninety "
        }
        return tyDict.get(num, "") 