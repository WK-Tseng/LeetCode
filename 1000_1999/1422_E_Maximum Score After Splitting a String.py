class Solution:
    def maxScore(self, s: str) -> int:
        scoreLeft = 0
        scoreRight = s.count('1')

        result = 0

        for c in s[:-1]:
            if c == '0':
                scoreLeft += 1
            else:
                scoreRight -= 1
            result = max(result, scoreLeft + scoreRight)

        return result
