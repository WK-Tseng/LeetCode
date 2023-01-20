class Solution:
    def numDecodings(self, s: str) -> int:
        
        decode_set = set([str(i+1) for i in range(26)])
        result = [1 if s[0] in decode_set else 0]

        if len(s) >= 2:
            count = 0
            if result[0] == 0:
                pass
            else:
                if s[1] in decode_set:
                    count += 1
                
                if s[0:2] in decode_set:
                    count += 1
            
            result.append(count)

        # print(result)

        for idx, c in enumerate(s[2:], 2):
            count = 0
            if s[idx] in decode_set:
                count += result[-1]
            
            if s[idx-1:idx+1] in decode_set:
                count += result[-2]

            result.append(count)

        # print(result)

        return result[-1]

