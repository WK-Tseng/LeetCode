class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        sp = sorted([weights[i] + weights[i+1] for i in range(len(weights)-1)])
        return sum(sp[len(sp) - k + 1:]) - sum(sp[:k - 1])