class Solution:
    def soupServings(self, n: int) -> float:
        
        if n > 5000:
            return 1

        @cache
        def servings(a, b):
            if a <= 0 and b <= 0:
                return 0.5
            
            if a <= 0:
                return 1
            
            if b <= 0:
                return 0

            probability = 0
            probability += servings(a - 100, b - 0)
            probability += servings(a - 75, b - 25)
            probability += servings(a - 50, b - 50)
            probability += servings(a - 25, b - 75)

            return probability * 0.25

        return servings(n, n)