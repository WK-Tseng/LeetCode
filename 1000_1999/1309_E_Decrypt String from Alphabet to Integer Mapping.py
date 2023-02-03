class Solution:
    def freqAlphabets(self, s: str) -> str:
        result = []
        temp = []
        for ss in s[::-1]:
            temp.append(ss)
            if temp[0] == '#':
                if len(temp) == 3:
                    result.insert(0, temp[2]+temp[1])
                    temp.clear()
            else:
                result.insert(0, temp[0])
                temp.clear()

        a_number = ord('a') - 1
        return ''.join(chr(a_number+int(ss)) for ss in result)