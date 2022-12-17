class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c in ['+', '-', '*', '/']:
                if c == '+':
                    stack[-2] = stack[-2] + stack[-1]
                elif c == '-':
                    stack[-2] = stack[-2] - stack[-1]
                elif c == '*':
                    stack[-2] = stack[-2] * stack[-1]
                elif c == '/':
                    stack[-2] = int(stack[-2] / stack[-1])
                stack = stack[:-1]
            else:
                stack.append(int(c))
        
        return stack[-1]