class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for c in s:
            if c == '*':
                stack.pop(-1)
            else:
                stack.append(c)
        return ''.join(stack)