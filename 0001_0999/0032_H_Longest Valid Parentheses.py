class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        maxLen = 0

        for idx, c in enumerate(s):
            if c == '(':
                stack.append(idx)
            else:
                del stack[-1]
                
                if len(stack) == 0:
                    stack.append(idx)
                else:
                    maxLen = max(maxLen, idx - stack[-1])
        return maxLen