class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        a, b = 'a', 'b'
        if x < y:
            x, y = y, x
            a, b = b, a

        count = Counter()
        result = 0

        for c in s + 'x':
            if c in 'ab':
                if c == b and count[a] > 0:
                    result += x
                    count[a] -= 1
                else:
                    count[c] += 1
            else:
                result += y * min(count[a], count[b])
                count = Counter()

        return result