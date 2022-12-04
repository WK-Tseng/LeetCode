class Solution:
    
    
    def letterCombinations(self, digits: str) -> List[str]:
        
        if len(digits) == 0:
            return []
        
        digits2letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        
        def Combo(digits, comboResult = "", level = 0, result = []):
        
            if level == len(digits):
                result.append(comboResult)
                return result


            for c in digits2letters[digits[level]]:
                result = Combo(digits, comboResult + c, level+1, result)

            return result
        
        
        
        return Combo(digits)
        
        
    