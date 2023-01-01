class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_list = [int(c) for c in a]
        b_list = [int(c) for c in b]

        a_len = len(a_list)
        b_len = len(b_list)

        if a_len > b_len:
            b_list = [0] * (a_len - b_len) + b_list
        elif a_len < b_len:
            a_list = [0] * (b_len - a_len) + a_list

        for i in range(len(a_list)):
            a_list[i] += b_list[i]

        for i in range(len(a_list)-1, -1, -1):
            c = a_list[i] // 2
            a_list[i] %= 2
            if c > 0:
                if i - 1 >= 0:
                    a_list[i-1] += 1
                else:
                    a_list.insert(0, 1)

        return ''.join([str(n) for n in a_list])