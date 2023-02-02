class Solution:
    def interpret(self, command: str) -> str:
        target_G = ['G']
        target_o = ['(', ')']
        target_al = ['(', 'a', 'l', ')']

        temp = []
        result = []
        for s in command:
            temp.append(s)
            if len(temp) == 1 and temp == target_G:
                result.append('G')
                temp.clear()
            elif len(temp) == 2 and temp == target_o:
                result.append('o')
                temp.clear()
            elif len(temp) == 4 and temp == target_al:
                result.append('al')
                temp.clear()

        return ''.join(result)
