class Solution:
    # ""
    # "******"

    # True
    # aaaabaaaabbbbaabbbaabbaababbabbaaaababaaabbbbbbaabbbabababbaaabaabaaaaaabbaabbbbaababbababaabbbaababbbba
    # *****b*aba***babaa*bbaba***a*aaba*b*aa**a*b**ba***a*a*
    
    # False
    # babbbbaabababaabbababaababaabbaabababbaaababbababaaaaaabbabaaaabababbabbababbbaaaababbbabbbbbbbbbbaabbb
    # b**bb**a**bba*b**a*bbb**aba***babbb*aa****aabb*bbb***a

    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False] * (len(p) + 1) for _ in range(2)]
        dp[0][0] = True
        for i in range(len(p)):
            if p[i] != '*':
                break
            dp[0][i+1] = True

        # print(dp)
        # print('------------')

        for i in range(len(s)):
            for j in range(len(p)):
                if p[j] in (s[i], '?'):
                    dp[1][j+1] = dp[0][j]
                elif p[j] == '*':
                    dp[1][j+1] = dp[0][j+1] or dp[1][j]
            
            dp[0], dp[1] = dp[1], [False] * (len(p) + 1)
            # print(dp)

        return dp[0][-1]
