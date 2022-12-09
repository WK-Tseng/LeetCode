class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []
        for num in range(left, right + 1):
            numStr = str(num)
            zero = any([c == '0' for c in numStr])
            if not zero:
                flag = True
                for c in numStr:
                    if num % int(c) != 0:
                        flag = False
                        break
                if flag:
                    result.append(num)
        
        return result
                