class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        sign = lambda x : x >= 0
        stack = []
        for asteroid in asteroids:
            while len(stack) > 0 and sign(stack[-1]) and not sign(asteroid):
                n1, n2 = abs(stack[-1]), abs(asteroid)
                if n1 == n2:
                    stack.pop(-1)
                    asteroid = None
                    break
                elif n1 > n2:
                    asteroid = None
                    break
                else:
                    stack.pop(-1)

            if asteroid is not None:
                stack.append(asteroid)
        return stack