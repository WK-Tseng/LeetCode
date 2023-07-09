class Solution:
    def largestVariance(self, s: str) -> int:
        counter = Counter(s)
        result = 0

        for a in counter:
            for b in counter:
                if a != b:
                    
                    aTimes, bTimes = 0, 0
                    aRemaining = counter[a]

                    for c in s:
                        if c == a:
                            aTimes += 1
                            aRemaining -= 1
                        elif c == b:
                            bTimes += 1

                        if bTimes < aTimes and aRemaining > 0:
                            aTimes, bTimes = 0, 0

                        if aTimes > 0 and bTimes > 0:
                            result = max(result, bTimes-aTimes)

        return result