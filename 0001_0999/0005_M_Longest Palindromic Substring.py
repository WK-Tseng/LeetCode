class Solution:
    # AC, fast
    def longestPalindrome(self, s: str) -> str:
        s_len = len(s)

        max_len = 0
        result = None

        for i in range(s_len):
            left, right = i, i

            while left-1 >= 0 and right+1 < s_len and s[left-1] == s[right+1]:
                left -= 1
                right += 1
            
            _len = right - left + 1
            if _len > max_len:
                max_len = _len
                result = s[left: right+1]

            left, right = i+1, i
            while left-1 >= 0 and right+1 < s_len and s[left-1] == s[right+1]:
                left -= 1
                right += 1

            _len = right - left + 1
            if _len > max_len:
                max_len = _len
                result = s[left: right+1]

        return result

    # AC, slow
    # def longestPalindrome(self, s: str) -> str:
    #     s_len = len(s)
    #     dp = [[False]*s_len for _ in range(s_len)]
    #     for i in range(s_len):
    #         dp[i][i] = True
        
    #     max_len = 1
    #     result = s[0]
    #     for y in range(s_len-1, -1, -1):
    #         for x in range(y+1, s_len):
    #             if s[y] == s[x] and (x == y+1 or dp[y+1][x-1]):
    #                 dp[y][x] = True
    #                 _len = x-y+1
    #                 if _len > max_len:
    #                     max_len = _len
    #                     result = s[y:y+_len]
    #     return result 

    # AC, slow
    # def longestPalindrome(self, s: str) -> str:
    #     dp = [[c==ss for ss in s] for c in s]
    #     s_len = len(s)

    #     start, max_len = None, 0

    #     for y in range(s_len):

    #         _len = 0
    #         flag = False
    #         for x in range(y+1):
    #             _y, _x = y-x, y+x 
    #             if _x < s_len and dp[_y][_x]:
    #                 _len += 2
    #             else:
    #                 if _len-1 > max_len:
    #                     flag = True
    #                 break
    #         else:
    #             if _len-1 > max_len:
    #                 flag = True

    #         if flag:
    #             max_len = _len - 1
    #             start = y - (max_len - 1) // 2
            
    #         _len = 0
    #         flag = False
    #         for x in range(y+1):
    #             _y, _x = y-x, y+x+1
    #             if _x < s_len and dp[_y][_x]:
    #                 _len += 2
    #             else:
    #                 if _len > max_len:
    #                     flag = True
    #                 break
    #         else:
    #             if _len > max_len:
    #                 flag = True
            
    #         if flag:
    #             max_len = _len
    #             start = y - max_len // 2 + 1


    #     return s[start:start+max_len]

    # AC, slow
    # def longestPalindrome(self, s: str) -> str:
    #     s_len = len(s)
    #     for l in range(s_len, 0, -1):
    #         for i in range(s_len-l+1):
    #             setp = l // 2
    #             if s[i] == s[i+l-1] and s[i:i+setp] == s[i+l-1:(i+l-1)-setp:-1]:
    #                 return s[i:i+l]

    #     return s[0]

    # AC, very slow
    # def longestPalindrome(self, s: str) -> str:
    #     sLen = len(s)
    #     ans = ""
    #     ansLen = 0
    #     for i in range(sLen):
    #         if i + ansLen <= sLen:
    #             for j in range(i+1+ansLen, sLen+1):
    #                 tempLen = j-i
    #                 if tempLen > ansLen:
    #                     temp = s[i:j]
    #                     if temp == temp[::-1]:
    #                         ans = temp
    #                         ansLen = len(temp)
                    
    #     return ans