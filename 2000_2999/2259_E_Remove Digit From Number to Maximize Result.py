class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        result = -1
        result_str = ''
        for i in range(len(number)):
            if number[i] == digit:
                temp = number[:i] + number[i+1:]
                temp_int = int(temp)
                if result < temp_int:
                    result = temp_int
                    result_str = temp

        return result_str