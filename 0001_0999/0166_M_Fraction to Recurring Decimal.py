class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        
        if numerator % denominator == 0:
            return str(numerator // denominator)

        sign = '' if numerator * denominator >= 0 else '-'

        numerator, denominator = abs(numerator), abs(denominator)
        result = sign + str(numerator//denominator) + '.'

        numerator %= denominator
        part = ''
        idx = 0
        rem_dict = {numerator: idx}
        
        while numerator % denominator:
            idx += 1
            numerator *= 10
            rem = numerator % denominator
            part += str(numerator//denominator)
            
            if rem in rem_dict:
                part = part[:rem_dict[rem]] + '(' + part[rem_dict[rem]:] + ')'
                return result + part

            rem_dict[rem] = idx
            numerator = rem

        return result + part