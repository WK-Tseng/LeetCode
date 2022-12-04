class Solution:
    def intToRomanSlice(self, Symbol, Step, num):
        
        ansStr = ""
        
        if num >= Step * 10:
            ansStr += Symbol[2]
            num -= Step * 10
            
        elif num >= Step * 9:
            ansStr += (Symbol[0] + Symbol[2])
            num -= Step * 9
        
        elif num >= Step * 5:
            temp = ""
            while num >= Step * 6:
                temp += Symbol[0]
                num -= Step
            
            ansStr += (Symbol[1] + temp)
            num -= Step * 5
            
        elif num >= Step * 4:
            ansStr += (Symbol[0] + Symbol[1])
            num -= Step * 4
        
        elif num >= Step * 1:
            while num >= Step * 1:
                ansStr += Symbol[0]
                num -= Step
                
        return ansStr, num
            
            
    
    def intToRoman(self, num: int) -> str:
        ansStr = ""
        
        while num >= 1000:
            ansStr += 'M'
            num -= 1000

        tempAns, num = self.intToRomanSlice(['C', 'D', 'M'], 100, num)
        ansStr += tempAns
        
        
        tempAns, num = self.intToRomanSlice(['X', 'L', 'C'], 10, num)
        ansStr += tempAns
        
        
        tempAns, num = self.intToRomanSlice(['I', 'V', 'X'], 1, num)
        ansStr += tempAns
        
        return ansStr
            