class Solution:
    def calculate(self, s: str) -> int:
        operators = ('+', '-', '*', '/')
        num_stack = []
        num = ''
        op = '+'

        idx = 0
        while idx < len(s):
            c = s[idx]

            if c in operators:
                _num = int(num)
                num = ''

                if op == '+':
                    num_stack.append(_num)
                elif op == '-':
                    num_stack.append(-_num)
                elif op == '*':
                    num_stack[-1] *= _num
                elif op == '/':
                    num_stack[-1] /= _num
                    num_stack[-1] = int(num_stack[-1])
                
                op = c
            else:
                num += c
            
            idx += 1

        # print(num_stack)
        # print(op)
        # print(num)

        _num = int(num)
        num = ''

        if op == '+':
            num_stack.append(_num)
        elif op == '-':
            num_stack.append(-_num)
        elif op == '*':
            num_stack[-1] *= _num
        elif op == '/':
            num_stack[-1] /= _num
            num_stack[-1] = int(num_stack[-1])
        
        return sum(num_stack)