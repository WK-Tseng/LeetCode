class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        len1, len2, len3 = len(s1), len(s2), len(s3)

        if len1 + len2 != len3:
            return False

        stack = [(0, 0)]
        visit = set()

        while stack:
            i, j = stack.pop(-1)

            if i+j == len3:
                return True

            if i < len1 and s1[i] == s3[i+j] and (i+1, j) not in visit:
                stack.append((i+1, j))
                visit.add((i+1, j))

            if j < len2 and s2[j] == s3[i+j] and (i, j+1) not in visit:
                stack.append((i, j+1))
                visit.add((i, j+1))

        return False

    # timeout
    # def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
    #     def f(s1, i, s2, j, s3):
    #         # print(s1, i, s2, j, s3)
    #         if len(s3) == 0 and len(s2) == 0 and len(s1) == 0:
    #             return True
            
    #         flag = False

    #         if len(s1) > 0 and len(s3) > 0 and s1[0] == s3[0]:
    #         # if abs((i+1)-j) <= 2 and len(s1) > 0 and len(s3) > 0 and s1[0] == s3[0]:
    #             flag |= f(s1[1:], i+1, s2, j, s3[1:])

    #         if len(s2) > 0 and len(s3) > 0 and s2[0] == s3[0]:
    #         # if abs(i-(j+1)) <= 2 and len(s2) > 0 and len(s3) > 0 and s2[0] == s3[0]:
    #             flag |= f(s1, i, s2[1:], j+1, s3[1:])

    #         return flag

    #     return f(s1, 0, s2, 0, s3)