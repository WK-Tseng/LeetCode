class Solution:
    def makeFancyString(self, s: str) -> str:
        stack = [[s[0], 1]]
        for c in s[1:]:
            if c == stack[-1][0]:
                cLen = stack[-1][1]
                # if cLen + 1 < 3:
                if cLen < 2:
                    stack[-1][1] += 1
            else:
                stack.append([c, 1])

        return ''.join([c*cLen for c, cLen in stack])