class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for c in s:
            if c in "([{":
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                else:
                    top = stack.pop()
                    flag = False
                    if top == '(' and c == ')':
                        flag = True
                    elif top == '[' and c == ']':
                        flag = True
                    elif top == '{' and c == '}':
                        flag = True

                    if not flag:
                        return False
        
        if len(stack) != 0:
            return False
        return True