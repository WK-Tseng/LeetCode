class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        counter = Counter()
        maxCount = 0
        result = 0

        for i in range(len(answerKey)):
            key = answerKey[i]
            counter[key] += 1
            maxCount = max(maxCount, counter[key])
            if result - maxCount < k:
                result += 1
            else:
                counter[answerKey[i-result]] -= 1
        
        return result