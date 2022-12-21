class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.lower()
        find_dot, find_e, find_num = False, False, False
        for i, c in enumerate(s):
            if c in ['+', '-']:
                if i > 0 and s[i-1] != 'e':
                    return False
            elif c == '.':
                if find_dot or find_e:
                    return False
                find_dot = True
            elif c == 'e':
                if find_e or not find_num:
                    return False
                find_e = True
                find_num = False
            elif c.isdigit():
                find_num = True
            else:
                return False
            # print(i, c, find_dot, find_e, find_num )
        return find_num