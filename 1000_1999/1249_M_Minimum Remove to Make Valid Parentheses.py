class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        parentheses = []

        for i, c in enumerate(s):
            if c in '()':
                parentheses.append((i, c))

        remove_stack = []

        for data in parentheses:
            if data[1] == '(':
                remove_stack.append(data)
            else:
                if len(remove_stack) == 0:
                    remove_stack.append(data)
                else:
                    if remove_stack[-1][1] == '(':
                        remove_stack.pop(-1)
                    else:
                        remove_stack.append(data)
        
        result = [c for c in s]
        for i, _ in remove_stack[::-1]:
            result.pop(i)

        return ''.join(result)
