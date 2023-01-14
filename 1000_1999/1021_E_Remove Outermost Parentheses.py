class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = []
        start = None
        left_count = 0
        
        for i, c in enumerate(s):
            if start is None:
                start = i
                left_count = 1
            else:
                left_count += 1 if c == '(' else -1
                if left_count == 0:
                    result.append(s[start+1 : i])
                    start = None
        
        return ''.join(result)
            
                        