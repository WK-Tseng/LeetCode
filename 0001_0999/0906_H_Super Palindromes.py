class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        min_num = int(left)
        max_num = int(right)

        min_num = pow(min_num, 0.5)
        max_num = pow(max_num, 0.5)

        int_min_num = int(min_num)
        int_max_num = int(max_num)

        min_num = int_min_num if min_num == int_min_num else (int_min_num + 1)
        max_num = int_max_num if max_num == int_max_num else int_max_num

        min_num_len = len(str(min_num))
        max_num_len = len(str(max_num))

        # print(min_num, max_num)
        # print(min_num_len, max_num_len)

        palindromes = set()
        def gen_pal(s, min_len, max_len, min_num, max_num):
            if len(s) > 0:
                left_s, mid_s = s[:-1], s[-1]
                temp = left_s + mid_s + left_s[::-1]
                if min_len <= len(temp) <= max_len and min_num <= int(temp) <= max_num:
                    palindromes.add(temp)
                
                temp = left_s + mid_s + mid_s + left_s[::-1]
                if min_len <= len(temp) <= max_len and min_num <= int(temp) <= max_num:
                    palindromes.add(temp)

            if len(s) * 2 < max_len:
                for i in range(10):
                    c = str(i)
                    gen_pal(s + c, min_len, max_len, min_num, max_num)

        gen_pal('', min_num_len, max_num_len, min_num, max_num)

        # print(palindromes)

        count = 0
        for p in palindromes:
            pp = int(p)**2
            pp_s = str(pp)
            if pp_s == pp_s[::-1]:
                count += 1

        return count